#!/bin/sh
SCRIPT_DIR=/opt/sac/scripts
export PYTHONPATH=/opt/sac  # needed for chronjob
echo script run >> /tmp/update_image
$SCRIPT_DIR/save_next_appointment.py
$SCRIPT_DIR/draw_on_pic.py
printimg $(python -c "from sac import config; print config.APP_CACHE_IMG")
