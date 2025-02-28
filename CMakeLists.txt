cmake_minimum_required(VERSION 3.26)

project( hydropi2c )

option( IS_RPI "" ON )

add_executable( hydropi2c )
configure_file( src/main.h.in main.h )
if( IS_RPI )
    target_include_directories( hydropi2c PRIVATE
        ext/pi_i2c/include
        ext/pi_i2c/src/config
        ext/pi_i2c/src/error
        ext/pi_i2c/src/utility )
    target_sources( hydropi2c PRIVATE
        ext/pi_i2c/src/config/config.c
        ext/pi_i2c/src/error/detect_recover_bus.c
        ext/pi_i2c/src/main/pi_i2c.c
        ext/pi_i2c/src/utility/clock_stretching.c
        ext/pi_i2c/src/utility/read_bus.c
        ext/pi_i2c/src/utility/write_bus.c
        ext/pi_i2c/src/utility/write_conditions_to_bus.c )
endif()
target_sources( hydropi2c PRIVATE
        src/main.cpp )
target_include_directories( hydropi2c PRIVATE ${CMAKE_CURRENT_BINARY_DIR} )
target_compile_definitions( hydropi2c PRIVATE _CRT_SECURE_NO_WARNINGS )