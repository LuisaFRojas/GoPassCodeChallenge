#!/bin/bash
        FECHA=$(date +%Y%m%d)
        ORIGEN="/home/usuario1"
        DESTINO="/backups/usuario1_backup_$FECHA.tar.gz"

        tar -czf "$DESTINO" "ORIGEN"
        echo "Backup generado en: $DESTINO"