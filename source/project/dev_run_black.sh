


black --version
echo "Black: Starting"

# Black project
echo "Black: project/"
black project/

# Black support
echo "Black: support/"
black support/

# Black tests
echo "Black: tests/"
black tests/

echo "Black: Complete!"