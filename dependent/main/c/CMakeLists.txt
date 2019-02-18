add_executable(c)
target_link_libraries(c PRIVATE my::a my::b)
target_sources(c
    PRIVATE
        c.cpp)
