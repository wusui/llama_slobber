#! /bin/bash
APPDIR=/home/wusui/llama_slobber/applications
TEMPDIR=`mktemp -d`
TEMPTAR=`mktemp`
NEW_TAR=`mktemp`
mkdir ${TEMPDIR}/generated_files
mkdir ${TEMPDIR}/question_data
cd ${APPDIR}
cp find_hun.py ${TEMPDIR}/find_hun.py
cd ${APPDIR}/question_data
tar cf ${TEMPTAR} .
cd ${TEMPDIR}/question_data
tar xf ${TEMPTAR}
echo "[DEFAULT]" > ${TEMPDIR}/logindata.ini
echo "username = foo" >> ${TEMPDIR}/logindata.ini
echo "password = bar" >> ${TEMPDIR}/logindata.ini
cd ${TEMPDIR}
tar cf ${NEW_TAR} .
cd ${APPDIR}
rm -rf ${TEMPDIR} ${TEMPTAR}
WEB_DIR=/home/wusui/warrensusui.com/public/llama_slobber.new
rm -rf ${WEB_DIR}
mkdir ${WEB_DIR}
mkdir ${WEB_DIR}/csv
mkdir ${WEB_DIR}/html
mkdir ${WEB_DIR}/tar
mv ${NEW_TAR} ${WEB_DIR}/tar/hun_values.tar
chmod 0644 ${WEB_DIR}/tar/hun_values.tar
cp ${APPDIR}/generated_files/cycle_data.html ${WEB_DIR}/html
cp ${APPDIR}/generated_files/mops.html ${WEB_DIR}/html
cp ${APPDIR}/generated_files/wonder.html ${WEB_DIR}/html
cp ${APPDIR}/generated_files/locations.csv ${WEB_DIR}/csv 
cp ${APPDIR}/generated_files/schools.csv ${WEB_DIR}/csv 
cp ${APPDIR}/generated_files/wonder.csv ${WEB_DIR}/csv 
cp ${APPDIR}/generated_files/mops.csv ${WEB_DIR}/csv 
cp ${APPDIR}/generated_files/wlt_cycles.csv ${WEB_DIR}/csv 
cp ${APPDIR}/web_pages/main_page.html ${WEB_DIR}
cd ${WEB_DIR}
cd ..
mv llama_slobber llama_slobber.old
mv llama_slobber.new llama_slobber
