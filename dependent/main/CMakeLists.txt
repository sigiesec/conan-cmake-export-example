project(dependent)
cmake_minimum_required(VERSION 3.9.0)

find_package(base REQUIRED)
add_subdirectory(c)

#export(EXPORT base NAMESPACE my)
install(TARGETS c
        EXPORT dependent
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        RUNTIME DESTINATION bin
        PUBLIC_HEADER DESTINATION include
       )
install(EXPORT dependent NAMESPACE my DESTINATION lib/dependent)
