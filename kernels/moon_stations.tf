KPL/FK

    Frames Specified by this Kernel
   =====================================================================

   Frame Name                  Relative to          Type   Frame ID
   -------------------------   -----------------    -----  --------
   MSTN-01                     MOON_PA              FIXED          31110

    Kernel Data
    ===================

    MOON_FIXED alias mapping
    -------------------------

\begindata

    TKFRAME_MOON_FIXED_RELATIVE = 'MOON_PA'
    TKFRAME_MOON_FIXED_SPEC = 'MATRIX'
    TKFRAME_MOON_FIXED_MATRIX = ( 1   0   0
                                  0   1   0
                                  0   0   1 )

\begintext

    PINPOINT output
    =====================

    Body-name mapping follows:

    \begindata

        NAIF_BODY_NAME          += 'MSTN-01'
        NAIF_BODY_CODE          +=  301001

    \begintext

    Reference frame specifications follow:

    Topocentric frame MSTN-01_TOPO

        The Z axis of this frame points towards the zenith.
        the X axis of this frame points North.

        Topocentric frame MSTN-01_TOPO is centered at the site MSTN-01, which at the epoch

            2022 FEB 27 00:00:00.000 TDB

        has Cartesian coordinates

            X (km):         0.000000E+4
            Y (km):         0.000000E+4
            Z (km):        -0.173597E+4

        and planetodetic coordinates

            Longitude (deg):    0.0000
            Latitude (deg):   -90.0000
            Altitude (deg):     0.0000

        These planetodetic coordinates are expressed relative to a reference spheroid having the dimensions

            Equatorial radius (km):     0.173710E+4
            Polar radius (km):          0.173597E+4

        All of the above coordinates are relative to the frame MOON_FIXED.

        \begindata

            FRAME_MSTN-01_TOPO              =   1301001
            FRAME_1301001_NAME              =   'MSTN-01_TOPO'
            FRAME_1301001_CLASS             =   4
            FRAME_1301001_CLASS_ID          =   1301001
            FRAME_1301001_CENTER            =   301001

            OBJECT_301001_FRAME             =   'MSTN-01_TOPO'

            TKFRAME_1301001_RELATIVE        =   'MOON_PA'
            TKFRAME_1301001_SPEC            =   'ANGLES'
            TKFRAME_1301001_UNITS           =   'DEGREES'
            TKFRAME_1301001_AXES            =   ( 3, 2, 3 )
            TKFRAME_1301001_ANGLES          =   (    0.0000,
                                                  -180.0000,
                                                   180.0000 )
        \begintext
