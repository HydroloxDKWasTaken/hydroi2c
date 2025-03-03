#include <cassert>
#include <cstdio>
#include "main.h"
#ifdef IS_RPI
extern "C"
{
#include <pi_i2c.h>
}
#endif

void i2c_setup( int sda, int scl )
{
    #ifdef IS_RPI
    if( auto e = config_i2c( sda, scl, I2C_STANDARD_MODE ); e != 0 )
        std::printf( "ERROR: config err %d\n", e );
    #endif
}

void i2c_read( int device_address, int register_address, int* data, int bytes )
{
    #ifdef IS_RPI
    if( auto e = read_i2c( device_address, register_address, data, bytes ); e != 0 )
        std::printf( "ERROR: read err %d\n", e );
    #endif
}

void write_file( std::FILE* f, int sensor1, int page_update_interval_ms )
{
    assert( f );
    std::fprintf( f, "<html>\n"
                     "<body>\n" );
    std::fprintf( f, "<script>"
                     "setTimeout( function() {"
                        "window.location.reload();"
                    "}, %d );", page_update_interval_ms );
    std::fprintf( f, "</script>" );
    std::fprintf( f, "qwrewyjkghmdfsa %d\n", sensor1 );
    std::fprintf( f, "</body>\n"
                     "</html>\n" );
}

int main()
{
    int dat = 250;
    i2c_setup( 1, 2 );
    i2c_read( 0, 15, &dat, 1 );
    write_file( std::fopen( "waaa.html", "w" ), dat, 2500 );
}