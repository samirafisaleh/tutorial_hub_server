
pylint --version

location=output_pylint.txt
echo "Pylint: Starting"
pylint . > $location
echo "Pylint: Complete. Please see $location"

