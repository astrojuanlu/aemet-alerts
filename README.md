# AEMET alerts

## Notes

https://opendata.aemet.es/dist/index.html#/avisos_cap/Avisos%20de%20Fen%C3%B3menos%20Meteorol%C3%B3gicos%20Adversos.%20%C3%9Altimo.

```
curl -X 'GET' \
  'https://opendata.aemet.es/opendata/api/avisos_cap/ultimoelaborado/area/esp' \
  -H 'accept: application/json' \
  -H 'api_key: $AEMET_API_KEY'
```

https://www.aemet.es/documentos/es/eltiempo/prediccion/avisos/plan_meteoalerta/METEOALERTA_ANX3_CAP.pdf
