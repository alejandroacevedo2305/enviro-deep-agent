select
  p.id,
  p.url,
  p.nombre,
  concat_ws('-', p.id, el.type, el.subtype, 'file_id_' || df.id::text) as file_identifier,
  df.metadata,
  df.s3_key,
  concat('https://443073691211-rq2lkjfg.us-west-2.console.aws.amazon.com/s3/object/nviro-crawlers?region=us-west-2&bucketType=general&prefix=', df.s3_key) as aws_url
from proyecto p
  join extracted_link el on p.id = el.fk_project_id
  join downloader.file df on el.id = df.fk_extracted_link_id
where
  -- formato de archivo soportado de momento
  df.file_format in ('pdf', 'docx', 'html')

  -- solo proyectos aprobados tipo DIA
  and p.estado = 'Aprobado'
  and p.tipo = 'DIA'

  -- filtro fecha
  and p.fecha_de_presentacion >= '2014-01-01'
  and p.fecha_de_presentacion < '2025-01-01'

  -- solo archivos clasificados
  and df.metadata->>'fileClass' is not null
order by p.fecha_de_presentacion desc, p.id, el.type, el.subtype, el.index, df.file_name;
