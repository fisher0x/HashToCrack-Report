Esta sección presenta un análisis de las credenciales extraídas durante el test de intrusión, centrándose únicamente en las cuentas de usuario habilitadas. Esto significa que se han omitido tanto las cuentas máquin, como aquellos usuarios que están deshabilitados.

Tal y como se muestra en la siguiente figura, de un total de **{{TOTAL_AMOUNT_OF_CREDS}}** credenciales obtenidas, **{{RECOVERED_AMOUNT_OF_CREDS}}** fueron recuperadas con éxito mediante un proceso de cracking de contraseñas offline llevado a cabo durante un periodo de 24 horas. Esto representa una tasa de recuperación del **{{RECOVERED_AMOUNT_OF_CREDS_PERCENTAGE}}**, lo que evidencia una exposición significativa de las credenciales de los usuarios.

![Estadísticas de Contraseñas Recuperadas](base64/imagedata)

Posteriormente, se realizó un análisis estadístico sobre el conjunto completo de credenciales obtenidas con el objetivo de identificar patrones comunes en la elección de contraseñas por parte de los usuarios. Tal y como se representa en la siguiente ilustración, la longitud de contraseña más frecuente fue de **{{HIGHEST_PASSWORD_LENGTH_DISTRIBUTION}}** caracteres, seguida de **{{SECOND_HIGHEST_PASSWORD_LENGTH_DISTRIBUTION}}** caracteres. Esta distribución sugiere una tendencia hacia longitudes de contraseña predecibles, lo que puede facilitar ataques de cracking.

![Distribución de Longitud de Contraseñas](base64/imagedata)

Adicionalmente, se llevó a cabo un análisis de complejidad de contraseñas para evaluar el grado de cumplimiento de una política de contraseñas robusta. A efectos de este estudio, una contraseña se consideró conforme si cumplía con los siguientes requisitos:
- Longitud mínima de 8 caracteres  
- Inclusión de al menos 3 de las siguientes 4 categorías:
  - Letras mayúsculas (A–Z)
  - Letras minúsculas (a–z)
  - Dígitos (0–9)
  - Caracteres especiales (!@#$%^&*…)

Tal y como se muestra en la siguiente figura, **{{COMPLIANCE_PASSWORD_PERCENTAGE}}** de las credenciales recuperadas cumplen con los requisitos anteriores. No obstante, el hecho de que dichas contraseñas hayan podido ser recuperadas indica que existe un margen de mejora, especialmente en aspectos como la unicidad de las contraseñas, la entropía y la resistencia frente a técnicas comunes de cracking.

![Análisis de Cumplimiento de Políticas](base64/imagedata)

Por último, se evaluó la reutilización de contraseñas dentro del dominio. Tal y como refleja la siguiente ilustración, se identificaron múltiples cuentas que comparten la misma contraseña. Este comportamiento incrementa significativamente el impacto de la posible compromisión de una única credencial y evidencia una política deficiente de higiene de contraseñas, facilitando movimientos laterales y posibles escaladas de privilegios dentro del entorno.

![Top 10 Contraseñas Más Usadas](base64/imagedata)
