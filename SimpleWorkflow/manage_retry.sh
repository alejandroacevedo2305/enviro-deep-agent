#!/bin/bash
# Enhanced Retry Process Management Script
#
# Usage:
#   ./manage_retry.sh start [options]   # Start background process
#   ./manage_retry.sh stop              # Stop gracefully
#   ./manage_retry.sh status            # Check status
#   ./manage_retry.sh logs              # Follow logs
#   ./manage_retry.sh force-stop        # Force kill (not recommended)
#
# Examples:
#   ./manage_retry.sh start
#   ./manage_retry.sh start --processing-workers 4
#   ./manage_retry.sh start --input-dir SimpleWorkflow/ParsingFailsSamples
#   ./manage_retry.sh status
#   ./manage_retry.sh logs
#   ./manage_retry.sh stop

set -e

# Configuration
PID_FILE="SimpleWorkflow/.retry_enhanced.pid"
LOG_FILE="SimpleWorkflow/retry_background.log"
SCRIPT="SimpleWorkflow/retry_failed_files_enhanced.py"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Helper functions
print_error() {
    echo -e "${RED}❌ $1${NC}"
}

print_success() {
    echo -e "${GREEN}✅ $1${NC}"
}

print_warning() {
    echo -e "${YELLOW}⚠️  $1${NC}"
}

print_info() {
    echo -e "${BLUE}ℹ️  $1${NC}"
}

# Check if process is running
is_running() {
    if [ -f "$PID_FILE" ]; then
        PID=$(cat "$PID_FILE")
        if ps -p "$PID" > /dev/null 2>&1; then
            return 0
        fi
    fi
    return 1
}

# Start command
cmd_start() {
    if is_running; then
        PID=$(cat "$PID_FILE")
        print_error "Process already running with PID $PID"
        echo ""
        print_info "Check status with: $0 status"
        print_info "Stop with: $0 stop"
        exit 1
    fi

    print_info "Starting enhanced retry process..."

    # Build command
    CMD="uv run python $SCRIPT"

    # Add any additional arguments
    if [ $# -gt 0 ]; then
        CMD="$CMD $*"
        print_info "Options: $*"
    fi

    # Start in background
    nohup $CMD > "$LOG_FILE" 2>&1 &
    PID=$!
    echo $PID > "$PID_FILE"

    # Wait a moment to see if it starts successfully
    sleep 2

    if is_running; then
        print_success "Background process started with PID $PID"
        echo ""
        print_info "Monitor with: $0 logs"
        print_info "Check status: $0 status"
        print_info "Stop with: $0 stop"
        echo ""
        print_info "Log file: $LOG_FILE"
    else
        print_error "Failed to start process"
        if [ -f "$LOG_FILE" ]; then
            echo ""
            print_info "Last 10 lines of log:"
            tail -10 "$LOG_FILE"
        fi
        exit 1
    fi
}

# Stop command
cmd_stop() {
    if ! is_running; then
        print_error "No process running"
        if [ -f "$PID_FILE" ]; then
            print_info "Removing stale PID file"
            rm "$PID_FILE"
        fi
        exit 1
    fi

    PID=$(cat "$PID_FILE")
    print_info "Stopping process $PID (graceful shutdown)..."

    kill $PID

    print_success "Stop signal sent (SIGTERM)"
    echo ""
    print_info "Waiting for graceful shutdown (max 120 seconds)..."

    # Wait up to 2 minutes for graceful shutdown
    for i in {1..120}; do
        if ! ps -p $PID > /dev/null 2>&1; then
            print_success "Process stopped gracefully after ${i}s"
            rm "$PID_FILE"
            return 0
        fi
        sleep 1

        # Show progress every 10 seconds
        if [ $((i % 10)) -eq 0 ]; then
            echo -n "."
        fi
    done

    echo ""
    print_warning "Process did not stop after 120s"
    print_info "Use '$0 force-stop' to force kill (not recommended)"
}

# Status command
cmd_status() {
    if ! is_running; then
        print_error "No process running"
        if [ -f "$PID_FILE" ]; then
            PID=$(cat "$PID_FILE")
            print_info "Stale PID file found (PID $PID)"
            print_info "Removing stale PID file"
            rm "$PID_FILE"
        fi
        exit 1
    fi

    PID=$(cat "$PID_FILE")
    print_success "Process running with PID $PID"
    echo ""

    # Process details
    echo "Process Details:"
    ps -p $PID -o pid,etime,rss,cmd --no-headers | \
        awk '{printf "  PID:         %s\n  Runtime:     %s\n  Memory:      %.1f MB\n  Command:     %s\n", $1, $2, $3/1024, substr($0, index($0,$4))}'
    echo ""

    # Recent progress from log
    if [ -f "$LOG_FILE" ]; then
        echo "Recent Progress:"
        grep "Retrying" "$LOG_FILE" | tail -3 | sed 's/^/  /'
        echo ""

        # Show successes and failures count
        SUCCESS=$(grep -c "✓" "$LOG_FILE" 2>/dev/null || echo "0")
        FAILURES=$(grep -c "✗" "$LOG_FILE" 2>/dev/null || echo "0")
        echo "Current Stats:"
        echo "  Successes:   $SUCCESS"
        echo "  Failures:    $FAILURES"

        if [ "$SUCCESS" -gt 0 ]; then
            TOTAL=$((SUCCESS + FAILURES))
            RATE=$(awk "BEGIN {printf \"%.1f\", ($SUCCESS / $TOTAL) * 100}")
            echo "  Success Rate: $RATE%"
        fi
    fi
}

# Logs command
cmd_logs() {
    if [ ! -f "$LOG_FILE" ]; then
        print_error "Log file not found: $LOG_FILE"
        exit 1
    fi

    print_info "Following log file: $LOG_FILE"
    print_info "Press Ctrl+C to stop"
    echo ""

    tail -f "$LOG_FILE"
}

# Force stop command
cmd_force_stop() {
    if ! is_running; then
        print_error "No process running"
        if [ -f "$PID_FILE" ]; then
            rm "$PID_FILE"
        fi
        exit 1
    fi

    PID=$(cat "$PID_FILE")
    print_warning "Force stopping process $PID (SIGKILL)"
    print_warning "This may leave temp files! Use regular stop when possible."

    kill -9 $PID 2>/dev/null || true

    sleep 1

    if ! ps -p $PID > /dev/null 2>&1; then
        print_success "Process force-stopped"
        rm "$PID_FILE"

        # Clean up temp files
        print_info "Cleaning up temp files..."
        rm -rf SimpleWorkflow/.temp_enhanced/* 2>/dev/null || true
        print_success "Cleanup complete"
    else
        print_error "Failed to stop process"
        exit 1
    fi
}

# Main command dispatcher
case "$1" in
    start)
        shift
        cmd_start "$@"
        ;;

    stop)
        cmd_stop
        ;;

    status)
        cmd_status
        ;;

    logs)
        cmd_logs
        ;;

    force-stop)
        cmd_force_stop
        ;;

    help|--help|-h)
        echo "Enhanced Retry Process Management Script"
        echo ""
        echo "Usage:"
        echo "  $0 start [options]   Start background retry process"
        echo "  $0 stop              Stop gracefully (recommended)"
        echo "  $0 status            Check process status"
        echo "  $0 logs              Follow log file"
        echo "  $0 force-stop        Force kill (use only if stop fails)"
        echo "  $0 help              Show this help"
        echo ""
        echo "Examples:"
        echo "  $0 start                                  # Start with defaults"
        echo "  $0 start --processing-workers 4           # Start with 4 workers"
        echo "  $0 start --input-dir path/to/failures     # Start with custom dir"
        echo "  $0 status                                 # Check if running"
        echo "  $0 logs                                   # Watch logs"
        echo "  $0 stop                                   # Stop gracefully"
        echo ""
        echo "Files:"
        echo "  PID file: $PID_FILE"
        echo "  Log file: $LOG_FILE"
        echo "  Script:   $SCRIPT"
        ;;

    *)
        print_error "Unknown command: $1"
        echo ""
        echo "Usage: $0 {start|stop|status|logs|force-stop|help}"
        echo "Run '$0 help' for more information"
        exit 1
        ;;
esac

