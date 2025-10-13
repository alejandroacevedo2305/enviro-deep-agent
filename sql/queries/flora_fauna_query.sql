select
  p.id,
  p.url,
  p.nombre,
  concat_ws('-', p.id, el.type, el.subtype, 'file_id_' || df.id::text) as file_identifier,
    df.metadata || jsonb_build_object('classes', json_agg(json_build_object(
    'class', fc.label,
    'confidence', rfc.confidence,
    'mode', fcm.label
  ))) as metadata_with_classes,
  df.s3_key,
  concat('https://443073691211-rq2lkjfg.us-west-2.console.aws.amazon.com/s3/object/nviro-crawlers?region=us-west-2&bucketType=general&prefix=', df.s3_key) as aws_url
from proyecto p
  join extracted_link el on p.id = el.fk_project_id
  join downloader.file df on el.id = df.fk_extracted_link_id
  join downloader.rel_file_class rfc on df.id = rfc.fk_file_id
  join downloader.file_class fc on rfc.fk_file_class_value = fc.value
  join downloader.file_classification_mode fcm on rfc.fk_file_classification_mode_value = fcm.value
where
  -- formato de archivo soportado de momento
  df.file_format in ('pdf', 'docx', 'html')

  -- solo proyectos aprobados tipo DIA
  and p.estado = 'Aprobado'
  and p.tipo = 'DIA'

  -- filtro fecha
  and p.fecha_de_presentacion >= '2014-01-01'
  --and p.fecha_de_presentacion < '2025-01-01'

  -- solo clases oficiales
  and fc.is_official

  and (
    (
      p.estado = 'Aprobado' -- solo proyectos aprobados de momento
      and (
        el.type like 'addendum-physics-files-%' or
        el.type like 'complementary-addendum-physics-files-%' or
        el.type = 'ei-document' or
        el.type = 'icsara' and el.subtype != 'desconocido'
      )
    ) or (
      el.subtype = 'anticipated-finished-resolution'
    )
  )
group by p.id, p.url, p.nombre, p.fecha_de_presentacion, el.type, el.subtype, el.index, df.id, df.file_name, df.metadata, df.s3_key
order by p.fecha_de_presentacion desc, p.id, el.type, el.subtype, el.index, df.file_name;
