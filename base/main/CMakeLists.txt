project(base)
cmake_minimum_required(VERSION 3.9.0)

add_subdirectory(a)
add_subdirectory(b)

#export(EXPORT base NAMESPACE my)
install(TARGETS a b 
        EXPORT base
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        PUBLIC_HEADER DESTINATION include
       )
install(EXPORT base NAMESPACE my:: DESTINATION lib/base/cmake)

include(CMakePackageConfigHelpers)
set(INCLUDE_INSTALL_DIR include)
configure_package_config_file(base-config.cmake.in
  ${CMAKE_CURRENT_BINARY_DIR}/base-config.cmake
  INSTALL_DESTINATION ${CMAKE_INSTALL_LIBDIR}/base/cmake
  PATH_VARS INCLUDE_INSTALL_DIR)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/base-config.cmake
        DESTINATION ${CMAKE_INSTALL_LIBDIR}/base/cmake )

