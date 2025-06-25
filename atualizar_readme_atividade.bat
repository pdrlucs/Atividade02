@echo off
cd /d "D:\Atividade Prática 02"

echo.
echo Iniciando atualização do README.md no GitHub...
echo.

git add README.md
git commit -m "Adicionando README.md da Atividade 02"
git push

echo.
echo ✅ Atualização concluída com sucesso!

echo.
echo Abrindo repositório no navegador...
start https://github.com/pdrlucs/Atividade02

pause
