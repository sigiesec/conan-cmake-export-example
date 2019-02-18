#!/bin/bash
set -x
set -e

echo CONAN_USE_WORKSPACE=$CONAN_USE_WORKSPACE
if [ "$CONAN_USE_WORKSPACE" == "false" ] ; then
  conan create base foo/bar
  conan create dependent foo/bar
fi
if [ "$CONAN_USE_WORKSPACE" == "true" ] ; then
  conan install . -if=build
  cat CMakeLists.txt
  cd build
  ${CONAN_CMAKE_PROGRAM} ..
  ${CONAN_CMAKE_PROGRAM} --build .
fi

