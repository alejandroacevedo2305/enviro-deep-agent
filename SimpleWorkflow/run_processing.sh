#!/bin/bash

# Robust PDF Processing Runner Script
# This script provides various ways to run the PDF processing with proper handling for long-running tasks

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default values
SCRIPT="SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py"
MAX_FILES=""
MODE="normal"
LOG_FILE="SimpleWorkflow/processing_$(date +%Y%m%d_%H%M%S).log"

# Function to print colored output
print_info() { echo -e "${BLUE}[INFO]${NC} $1"; }
print_success() { echo -e "${GREEN}[SUCCESS]${NC} $1"; }
print_warning() { echo -e "${YELLOW}[WARNING]${NC} $1"; }
print_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Function to show usage
show_usage() {
    cat << EOF
Usage: $0 [OPTIONS]

Run PDF processing script with various modes for handling long-running tasks.

OPTIONS:
    -h, --help              Show this help message
    -m, --mode MODE         Processing mode (default: normal)
                           Modes:
                           - normal: Run in foreground
                           - background: Run with nohup in background
                           - screen: Run in screen session
                           - tmux: Run in tmux session
    -f, --max-files NUM    Maximum number of files to process
    -r, --resume           Resume from previous state
    --retry-failed         Retry only failed files
    --timeout SECONDS      Timeout per file (default: 300)
    --memory-limit MB      Memory limit before GC (default: 4000)
    --workers NUM          Number of parallel workers (async version only)
    --script SCRIPT        Script to run (robust/sync/async)
                           - robust: sql_metadata_to_parsed_markdown_robust.py (default)
                           - sync: sql_metadata_to_parsed_markdown.py
                           - async: sql_metadata_to_parsed_markdown_async.py

EXAMPLES:
    # Process 100 files in background
    $0 --mode background --max-files 100

    # Resume processing in screen session
    $0 --mode screen --resume

    # Process all files with tmux
    $0 --mode tmux

    # Monitor background job
    $0 --status

EOF
}

# Function to check if process is running
check_process() {
    local pid_file="SimpleWorkflow/.processing.pid"
    if [ -f "$pid_file" ]; then
        local pid=$(cat "$pid_file")
        if ps -p "$pid" > /dev/null 2>&1; then
            print_info "Process is running (PID: $pid)"
            print_info "Check logs: tail -f SimpleWorkflow/processing_robust.log"
            return 0
        else
            print_warning "Process not running (stale PID file)"
            rm -f "$pid_file"
            return 1
        fi
    else
        print_info "No process running"
        return 1
    fi
}

# Parse arguments
ARGS=""
while [[ $# -gt 0 ]]; do
    case $1 in
        -h|--help)
            show_usage
            exit 0
            ;;
        -m|--mode)
            MODE="$2"
            shift 2
            ;;
        -f|--max-files)
            MAX_FILES="--max-files $2"
            shift 2
            ;;
        -r|--resume)
            ARGS="$ARGS --resume"
            shift
            ;;
        --retry-failed)
            # For retry-failed, use the original script as it has this feature
            SCRIPT="SimpleWorkflow/sql_metadata_to_parsed_markdown.py"
            ARGS="$ARGS --retry-failed"
            shift
            ;;
        --timeout)
            ARGS="$ARGS --timeout $2"
            shift 2
            ;;
        --memory-limit)
            ARGS="$ARGS --memory-limit $2"
            shift 2
            ;;
        --workers)
            SCRIPT="SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py"
            ARGS="$ARGS --workers $2"
            shift 2
            ;;
        --script)
            case $2 in
                robust)
                    SCRIPT="SimpleWorkflow/sql_metadata_to_parsed_markdown_robust.py"
                    ;;
                sync)
                    SCRIPT="SimpleWorkflow/sql_metadata_to_parsed_markdown.py"
                    ;;
                async)
                    SCRIPT="SimpleWorkflow/sql_metadata_to_parsed_markdown_async.py"
                    ;;
                *)
                    print_error "Invalid script: $2"
                    exit 1
                    ;;
            esac
            shift 2
            ;;
        --status)
            check_process
            exit $?
            ;;
        *)
            print_error "Unknown option: $1"
            show_usage
            exit 1
            ;;
    esac
done

# Build command
CMD="uv run python $SCRIPT $MAX_FILES $ARGS"

print_info "Script: $SCRIPT"
print_info "Command: $CMD"
print_info "Mode: $MODE"

# Run based on mode
case $MODE in
    normal)
        print_info "Running in foreground..."
        print_info "Press Ctrl+C to stop gracefully"
        $CMD
        ;;

    background)
        print_info "Running in background with nohup..."
        print_info "Logs will be written to: $LOG_FILE"

        # Save PID for monitoring
        nohup $CMD > "$LOG_FILE" 2>&1 &
        PID=$!
        echo $PID > SimpleWorkflow/.processing.pid

        print_success "Started process (PID: $PID)"
        print_info "Monitor with: tail -f $LOG_FILE"
        print_info "Check status with: $0 --status"
        print_info "Stop with: kill -TERM $PID"
        ;;

    screen)
        # Check if screen is installed
        if ! command -v screen &> /dev/null; then
            print_error "screen is not installed. Install with: sudo apt-get install screen"
            exit 1
        fi

        SESSION_NAME="pdf_processing"
        print_info "Starting in screen session: $SESSION_NAME"

        # Kill existing session if exists
        screen -S $SESSION_NAME -X quit 2>/dev/null || true

        # Start new session
        screen -dmS $SESSION_NAME bash -c "$CMD; echo 'Process finished. Press any key to exit.'; read -n 1"

        print_success "Started screen session: $SESSION_NAME"
        print_info "Attach with: screen -r $SESSION_NAME"
        print_info "Detach with: Ctrl+A, D"
        print_info "List sessions: screen -ls"
        ;;

    tmux)
        # Check if tmux is installed
        if ! command -v tmux &> /dev/null; then
            print_error "tmux is not installed. Install with: sudo apt-get install tmux"
            exit 1
        fi

        SESSION_NAME="pdf_processing"
        print_info "Starting in tmux session: $SESSION_NAME"

        # Kill existing session if exists
        tmux kill-session -t $SESSION_NAME 2>/dev/null || true

        # Start new session
        tmux new-session -d -s $SESSION_NAME "$CMD; echo 'Process finished. Press any key to exit.'; read -n 1"

        print_success "Started tmux session: $SESSION_NAME"
        print_info "Attach with: tmux attach -t $SESSION_NAME"
        print_info "Detach with: Ctrl+B, D"
        print_info "List sessions: tmux ls"
        ;;

    *)
        print_error "Invalid mode: $MODE"
        show_usage
        exit 1
        ;;
esac

# Additional tips
if [ "$MODE" != "normal" ]; then
    echo ""
    print_info "=== Tips for long-running processes ==="
    print_info "1. Use 'htop' or 'top' to monitor system resources"
    print_info "2. Check processing state: cat SimpleWorkflow/.processing_state.json"
    print_info "3. Count processed files: ls SimpleWorkflow/ParsedFiles/*.md | wc -l"
    print_info "4. Count failed files: ls SimpleWorkflow/ParsedFiles/FAILED-*.md | wc -l"
    print_info "5. View recent logs: tail -n 50 SimpleWorkflow/processing_robust.log"
fi
