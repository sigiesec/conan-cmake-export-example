add_library(a SHARED)
target_sources(a
    PUBLIC
        $<BUILD_INTERFACE:${CMAKE_CURRENT_LIST_DIR}/a.h>
        $<INSTALL_INTERFACE:include/a.h>
    PRIVATE
        a.cpp)
set_target_properties(a PROPERTIES PUBLIC_HEADER "${CMAKE_CURRENT_LIST_DIR}/a.h")
target_include_directories(a INTERFACE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}>
  $<INSTALL_INTERFACE:include>
)

