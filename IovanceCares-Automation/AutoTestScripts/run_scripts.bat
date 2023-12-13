@echo off

python PatientRegistration.py > output.log 2>&1 || echo "script1.py failed, but continuing..."
python ApproveTILOrderRequest.py >> output.log 2>&1



