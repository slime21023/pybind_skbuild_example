
cmake_minimum_required(VERSION 3.15...3.26)

project(${SKBUILD_PROJECT_NAME} VERSION ${SKBUILD_PROJECT_VERSION})

find_package(Python 3.8 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(example MODULE src/main.cpp)
target_compile_definitions(example PRIVATE VERSION_INFO=${PROJECT_VERSION})

install(TARGETS example DESTINATION scikit_build_example)