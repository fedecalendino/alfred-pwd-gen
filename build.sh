function build() {
  echo "Generating binary file for $1"
  echo

  poetry run python3 -m nuitka --onefile "src/$1.py"

  echo
  echo "Cleaning up nuitka temporary files..."
   rm -rf "$1.build/"
   rm -rf "$1.dist/"
   rm -rf "$1.onefile-build/"

	 mkdir bin 2> /dev/null
	 mv "$1.bin" "./bin/$1"

  echo
	echo "Finished generating bin file for $1"
}

build main
