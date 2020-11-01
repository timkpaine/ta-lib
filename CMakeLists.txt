cmake_minimum_required(VERSION 3.7.2)
project(ta_lib C)
set(CMAKE_BUILD_TYPE "Release")
set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

if(NOT DEFINED TALIB_CMAKE_MODULE_PATH)
	set(TALIB_CMAKE_MODULE_PATH "${CMAKE_SOURCE_DIR}/cmake/")
endif()
set(CMAKE_MODULE_PATH "${TALIB_CMAKE_MODULE_PATH}/modules" ${CMAKE_MODULE_PATH})

if(${CMAKE_SYSTEM_NAME} MATCHES "Windows")
	set(WIN32 ON)
    set(MACOS OFF)
    set(LINUX OFF)
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(WIN32 OFF)
    set(MACOS ON)
    set(LINUX OFF)
else()
    set(WIN32 OFF)
    set(MACOS OFF)
    set(LINUX ON)
endif()

###############################
# Helper to grab dependencies #
###############################
function (build_dep name cmake_file)
	if(EXISTS ${CMAKE_BINARY_DIR}/${name}-src)
        message("${Cyan}Dependency found - not rebuilding - ${CMAKE_BINARY_DIR}/${name}-src${ColorReset}")
	else()
		configure_file(${cmake_file} ${name}-download/CMakeLists.txt)

		execute_process(COMMAND ${CMAKE_COMMAND} -G "${CMAKE_GENERATOR}" .
			RESULT_VARIABLE result
			WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/${name}-download )

		if(result)
			message(FATAL_ERROR "CMake step for ${name} failed: ${result}")
		endif()

		execute_process(COMMAND ${CMAKE_COMMAND} --build .
			RESULT_VARIABLE result
			WORKING_DIRECTORY ${CMAKE_BINARY_DIR}/${name}-download )

		if(result)
			message(FATAL_ERROR "Build step for ${name} failed: ${result}")
		endif()
endif()
endfunction()
##############################

#######################
# BUILD CONFIGURATION #
#######################
find_package(Color)
option(CMAKE_BUILD_TYPE "Release/Debug build" RELEASE)
option(BUILD_TESTS "Build regression tests" ON)

if(DEFINED ENV{DEBUG})
	set(CMAKE_BUILD_TYPE DEBUG)
else()
	if (NOT DEFINED CMAKE_BUILD_TYPE)
		set(CMAKE_BUILD_TYPE RELEASE)
	endif()
endif()

if(NOT WIN32)
	set(CMAKE_SHARED_LIBRARY_SUFFIX .so)
	set(CMAKE_C_FLAGS "-O3 -DNDEBUG -Wall -W -fno-strict-aliasing -D_REENTRANT -DQT_THREAD_SUPPORT")
else()
	cmake_policy(SET CMP0074 NEW)
	set(CMAKE_C_FLAGS " /EHsc /MP /MD /DWIN32 /D_MBCS /D_LIB /DQT_THREAD_SUPPORT")
	set(CMAKE_SHARED_LIBRARY_PREFIX lib)
endif()

build_dep("ta-lib-src" "${TALIB_CMAKE_MODULE_PATH}/talib.txt.in")
##############################

set(TALIB_abstract_src
	ta-lib-src/src/ta_abstract/ta_abstract.c
	ta-lib-src/src/ta_abstract/ta_def_ui.c
	ta-lib-src/src/ta_abstract/ta_func_api.c
	ta-lib-src/src/ta_abstract/ta_group_idx.c
	ta-lib-src/src/ta_abstract/frames/ta_frame.c
	ta-lib-src/src/ta_abstract/tables/table_a.c
	ta-lib-src/src/ta_abstract/tables/table_b.c
	ta-lib-src/src/ta_abstract/tables/table_c.c
	ta-lib-src/src/ta_abstract/tables/table_d.c
	ta-lib-src/src/ta_abstract/tables/table_e.c
	ta-lib-src/src/ta_abstract/tables/table_f.c
	ta-lib-src/src/ta_abstract/tables/table_g.c
	ta-lib-src/src/ta_abstract/tables/table_h.c
	ta-lib-src/src/ta_abstract/tables/table_i.c
	ta-lib-src/src/ta_abstract/tables/table_j.c
	ta-lib-src/src/ta_abstract/tables/table_k.c
	ta-lib-src/src/ta_abstract/tables/table_l.c
	ta-lib-src/src/ta_abstract/tables/table_m.c
	ta-lib-src/src/ta_abstract/tables/table_n.c
	ta-lib-src/src/ta_abstract/tables/table_o.c
	ta-lib-src/src/ta_abstract/tables/table_p.c
	ta-lib-src/src/ta_abstract/tables/table_q.c
	ta-lib-src/src/ta_abstract/tables/table_r.c
	ta-lib-src/src/ta_abstract/tables/table_s.c
	ta-lib-src/src/ta_abstract/tables/table_t.c
	ta-lib-src/src/ta_abstract/tables/table_u.c
	ta-lib-src/src/ta_abstract/tables/table_v.c
	ta-lib-src/src/ta_abstract/tables/table_w.c
	ta-lib-src/src/ta_abstract/tables/table_x.c
	ta-lib-src/src/ta_abstract/tables/table_y.c
	ta-lib-src/src/ta_abstract/tables/table_z.c
)

set(TALIB_common_src 
	ta-lib-src/src/ta_common/ta_global.c
	ta-lib-src/src/ta_common/ta_retcode.c
	ta-lib-src/src/ta_common/ta_version.c
)

set(TALIB_func_src
	ta-lib-src/src/ta_func/ta_utility.c
	ta-lib-src/src/ta_func/ta_ACOS.c
	ta-lib-src/src/ta_func/ta_AD.c
	ta-lib-src/src/ta_func/ta_ADD.c
	ta-lib-src/src/ta_func/ta_ADOSC.c
	ta-lib-src/src/ta_func/ta_ADX.c
	ta-lib-src/src/ta_func/ta_ADXR.c
	ta-lib-src/src/ta_func/ta_APO.c
	ta-lib-src/src/ta_func/ta_AROON.c
	ta-lib-src/src/ta_func/ta_AROONOSC.c
	ta-lib-src/src/ta_func/ta_ASIN.c
	ta-lib-src/src/ta_func/ta_ATAN.c
	ta-lib-src/src/ta_func/ta_ATR.c
	ta-lib-src/src/ta_func/ta_AVGPRICE.c
	ta-lib-src/src/ta_func/ta_BBANDS.c
	ta-lib-src/src/ta_func/ta_BETA.c
	ta-lib-src/src/ta_func/ta_BOP.c
	ta-lib-src/src/ta_func/ta_CCI.c
	ta-lib-src/src/ta_func/ta_CDL2CROWS.c
	ta-lib-src/src/ta_func/ta_CDL3BLACKCROWS.c
	ta-lib-src/src/ta_func/ta_CDL3INSIDE.c
	ta-lib-src/src/ta_func/ta_CDL3LINESTRIKE.c
	ta-lib-src/src/ta_func/ta_CDL3OUTSIDE.c
	ta-lib-src/src/ta_func/ta_CDL3STARSINSOUTH.c
	ta-lib-src/src/ta_func/ta_CDL3WHITESOLDIERS.c
	ta-lib-src/src/ta_func/ta_CDLABANDONEDBABY.c
	ta-lib-src/src/ta_func/ta_CDLADVANCEBLOCK.c
	ta-lib-src/src/ta_func/ta_CDLBELTHOLD.c
	ta-lib-src/src/ta_func/ta_CDLBREAKAWAY.c
	ta-lib-src/src/ta_func/ta_CDLCLOSINGMARUBOZU.c
	ta-lib-src/src/ta_func/ta_CDLCONCEALBABYSWALL.c
	ta-lib-src/src/ta_func/ta_CDLCOUNTERATTACK.c
	ta-lib-src/src/ta_func/ta_CDLDARKCLOUDCOVER.c
	ta-lib-src/src/ta_func/ta_CDLDOJI.c
	ta-lib-src/src/ta_func/ta_CDLDOJISTAR.c
	ta-lib-src/src/ta_func/ta_CDLDRAGONFLYDOJI.c
	ta-lib-src/src/ta_func/ta_CDLENGULFING.c
	ta-lib-src/src/ta_func/ta_CDLEVENINGDOJISTAR.c
	ta-lib-src/src/ta_func/ta_CDLEVENINGSTAR.c
	ta-lib-src/src/ta_func/ta_CDLGAPSIDESIDEWHITE.c
	ta-lib-src/src/ta_func/ta_CDLGRAVESTONEDOJI.c
	ta-lib-src/src/ta_func/ta_CDLHAMMER.c
	ta-lib-src/src/ta_func/ta_CDLHANGINGMAN.c
	ta-lib-src/src/ta_func/ta_CDLHARAMI.c
	ta-lib-src/src/ta_func/ta_CDLHARAMICROSS.c
	ta-lib-src/src/ta_func/ta_CDLHIGHWAVE.c
	ta-lib-src/src/ta_func/ta_CDLHIKKAKE.c
	ta-lib-src/src/ta_func/ta_CDLHIKKAKEMOD.c
	ta-lib-src/src/ta_func/ta_CDLHOMINGPIGEON.c
	ta-lib-src/src/ta_func/ta_CDLIDENTICAL3CROWS.c
	ta-lib-src/src/ta_func/ta_CDLINNECK.c
	ta-lib-src/src/ta_func/ta_CDLINVERTEDHAMMER.c
	ta-lib-src/src/ta_func/ta_CDLKICKING.c
	ta-lib-src/src/ta_func/ta_CDLKICKINGBYLENGTH.c
	ta-lib-src/src/ta_func/ta_CDLLADDERBOTTOM.c
	ta-lib-src/src/ta_func/ta_CDLLONGLEGGEDDOJI.c
	ta-lib-src/src/ta_func/ta_CDLLONGLINE.c
	ta-lib-src/src/ta_func/ta_CDLMARUBOZU.c
	ta-lib-src/src/ta_func/ta_CDLMATCHINGLOW.c
	ta-lib-src/src/ta_func/ta_CDLMATHOLD.c
	ta-lib-src/src/ta_func/ta_CDLMORNINGDOJISTAR.c
	ta-lib-src/src/ta_func/ta_CDLMORNINGSTAR.c
	ta-lib-src/src/ta_func/ta_CDLONNECK.c
	ta-lib-src/src/ta_func/ta_CDLPIERCING.c
	ta-lib-src/src/ta_func/ta_CDLRICKSHAWMAN.c
	ta-lib-src/src/ta_func/ta_CDLRISEFALL3METHODS.c
	ta-lib-src/src/ta_func/ta_CDLSEPARATINGLINES.c
	ta-lib-src/src/ta_func/ta_CDLSHOOTINGSTAR.c
	ta-lib-src/src/ta_func/ta_CDLSHORTLINE.c
	ta-lib-src/src/ta_func/ta_CDLSPINNINGTOP.c
	ta-lib-src/src/ta_func/ta_CDLSTALLEDPATTERN.c
	ta-lib-src/src/ta_func/ta_CDLSTICKSANDWICH.c
	ta-lib-src/src/ta_func/ta_CDLTAKURI.c
	ta-lib-src/src/ta_func/ta_CDLTASUKIGAP.c
	ta-lib-src/src/ta_func/ta_CDLTHRUSTING.c
	ta-lib-src/src/ta_func/ta_CDLTRISTAR.c
	ta-lib-src/src/ta_func/ta_CDLUNIQUE3RIVER.c
	ta-lib-src/src/ta_func/ta_CDLUPSIDEGAP2CROWS.c
	ta-lib-src/src/ta_func/ta_CDLXSIDEGAP3METHODS.c
	ta-lib-src/src/ta_func/ta_CEIL.c
	ta-lib-src/src/ta_func/ta_CMO.c
	ta-lib-src/src/ta_func/ta_CORREL.c
	ta-lib-src/src/ta_func/ta_COS.c
	ta-lib-src/src/ta_func/ta_COSH.c
	ta-lib-src/src/ta_func/ta_DEMA.c
	ta-lib-src/src/ta_func/ta_DIV.c
	ta-lib-src/src/ta_func/ta_DX.c
	ta-lib-src/src/ta_func/ta_EMA.c
	ta-lib-src/src/ta_func/ta_EXP.c
	ta-lib-src/src/ta_func/ta_FLOOR.c
	ta-lib-src/src/ta_func/ta_HT_DCPERIOD.c
	ta-lib-src/src/ta_func/ta_HT_DCPHASE.c
	ta-lib-src/src/ta_func/ta_HT_PHASOR.c
	ta-lib-src/src/ta_func/ta_HT_SINE.c
	ta-lib-src/src/ta_func/ta_HT_TRENDLINE.c
	ta-lib-src/src/ta_func/ta_HT_TRENDMODE.c
	ta-lib-src/src/ta_func/ta_KAMA.c
	ta-lib-src/src/ta_func/ta_LINEARREG.c
	ta-lib-src/src/ta_func/ta_LINEARREG_ANGLE.c
	ta-lib-src/src/ta_func/ta_LINEARREG_INTERCEPT.c
	ta-lib-src/src/ta_func/ta_LINEARREG_SLOPE.c
	ta-lib-src/src/ta_func/ta_LN.c
	ta-lib-src/src/ta_func/ta_LOG10.c
	ta-lib-src/src/ta_func/ta_MA.c
	ta-lib-src/src/ta_func/ta_MACD.c
	ta-lib-src/src/ta_func/ta_MACDEXT.c
	ta-lib-src/src/ta_func/ta_MACDFIX.c
	ta-lib-src/src/ta_func/ta_MAMA.c
	ta-lib-src/src/ta_func/ta_MAVP.c
	ta-lib-src/src/ta_func/ta_MAX.c
	ta-lib-src/src/ta_func/ta_MAXINDEX.c
	ta-lib-src/src/ta_func/ta_MEDPRICE.c
	ta-lib-src/src/ta_func/ta_MFI.c
	ta-lib-src/src/ta_func/ta_MIDPOINT.c
	ta-lib-src/src/ta_func/ta_MIDPRICE.c
	ta-lib-src/src/ta_func/ta_MIN.c
	ta-lib-src/src/ta_func/ta_MININDEX.c
	ta-lib-src/src/ta_func/ta_MINMAX.c
	ta-lib-src/src/ta_func/ta_MINMAXINDEX.c
	ta-lib-src/src/ta_func/ta_MINUS_DI.c
	ta-lib-src/src/ta_func/ta_MINUS_DM.c
	ta-lib-src/src/ta_func/ta_MOM.c
	ta-lib-src/src/ta_func/ta_MULT.c
	ta-lib-src/src/ta_func/ta_NATR.c
	ta-lib-src/src/ta_func/ta_OBV.c
	ta-lib-src/src/ta_func/ta_PLUS_DI.c
	ta-lib-src/src/ta_func/ta_PLUS_DM.c
	ta-lib-src/src/ta_func/ta_PPO.c
	ta-lib-src/src/ta_func/ta_ROC.c
	ta-lib-src/src/ta_func/ta_ROCP.c
	ta-lib-src/src/ta_func/ta_ROCR.c
	ta-lib-src/src/ta_func/ta_ROCR100.c
	ta-lib-src/src/ta_func/ta_RSI.c
	ta-lib-src/src/ta_func/ta_SAR.c
	ta-lib-src/src/ta_func/ta_SAREXT.c
	ta-lib-src/src/ta_func/ta_SIN.c
	ta-lib-src/src/ta_func/ta_SINH.c
	ta-lib-src/src/ta_func/ta_SMA.c
	ta-lib-src/src/ta_func/ta_SQRT.c
	ta-lib-src/src/ta_func/ta_STDDEV.c
	ta-lib-src/src/ta_func/ta_STOCH.c
	ta-lib-src/src/ta_func/ta_STOCHF.c
	ta-lib-src/src/ta_func/ta_STOCHRSI.c
	ta-lib-src/src/ta_func/ta_SUB.c
	ta-lib-src/src/ta_func/ta_SUM.c
	ta-lib-src/src/ta_func/ta_T3.c
	ta-lib-src/src/ta_func/ta_TAN.c
	ta-lib-src/src/ta_func/ta_TANH.c
	ta-lib-src/src/ta_func/ta_TEMA.c
	ta-lib-src/src/ta_func/ta_TRANGE.c
	ta-lib-src/src/ta_func/ta_TRIMA.c
	ta-lib-src/src/ta_func/ta_TRIX.c
	ta-lib-src/src/ta_func/ta_TSF.c
	ta-lib-src/src/ta_func/ta_TYPPRICE.c
	ta-lib-src/src/ta_func/ta_ULTOSC.c
	ta-lib-src/src/ta_func/ta_VAR.c
	ta-lib-src/src/ta_func/ta_WCLPRICE.c
	ta-lib-src/src/ta_func/ta_WILLR.c
	ta-lib-src/src/ta_func/ta_WMA.c
)

set(TALIB_test_src
	ta-lib-src/src/tools/ta_regtest/ta_regtest.c
	ta-lib-src/src/tools/ta_regtest/test_data.c
	ta-lib-src/src/tools/ta_regtest/test_util.c
	ta-lib-src/src/tools/ta_regtest/test_abstract.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_adx.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_mom.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_sar.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_rsi.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_candlestick.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_per_ema.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_per_hlc.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_stoch.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_macd.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_minmax.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_per_hlcv.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_1in_1out.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_1in_2out.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_per_ohlc.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_stddev.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_bbands.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_ma.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_po.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_per_hl.c
	ta-lib-src/src/tools/ta_regtest/ta_test_func/test_trange.c
	ta-lib-src/src/tools/ta_regtest/test_internals.c
)

set(TALIB_install_headers
	${CMAKE_BINARY_DIR}/ta-lib-src/include/ta_abstract.h
	${CMAKE_BINARY_DIR}/ta-lib-src/include/ta_common.h
	${CMAKE_BINARY_DIR}/ta-lib-src/include/ta_defs.h
	${CMAKE_BINARY_DIR}/ta-lib-src/include/ta_func.h
	${CMAKE_BINARY_DIR}/ta-lib-src/include/ta_libc.h
)

include_directories(${CMAKE_BINARY_DIR}/ta-lib-src/include/)
include_directories(${CMAKE_BINARY_DIR}/ta-lib-src/src/ta_common/)
include_directories(${CMAKE_BINARY_DIR}/ta-lib-src/src/ta_abstract/)
include_directories(${CMAKE_BINARY_DIR}/ta-lib-src/src/ta_abstract/frames)
include_directories(${CMAKE_BINARY_DIR}/ta-lib-src/src/ta_func/)
add_library(ta_lib SHARED ${TALIB_abstract_src} ${TALIB_common_src} ${TALIB_func_src})

install(TARGETS ta_lib LIBRARY DESTINATION lib)
install(FILES ${TALIB_install_headers} DESTINATION include)

if(BUILD_TESTS)
	# tests
	add_executable(ta_regtest ${TALIB_test_src})
	target_include_directories(ta_regtest PRIVATE ${CMAKE_BINARY_DIR}/ta-lib-src/src/tools/ta_regtest/)
	target_link_libraries(ta_regtest ta_lib)
endif()
