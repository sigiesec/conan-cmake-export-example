add_library(b STATIC)
target_sources(b
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/b.h>
        $<INSTALL_INTERFACE:include/b.h>
    PRIVATE
        b.cpp)
set_target_properties(b PROPERTIES PUBLIC_HEADER "${CMAKE_CURRENT_LIST_DIR}/b.h")
target_include_directories(b INTERFACE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
  $<INSTALL_INTERFACE:include>  
)
