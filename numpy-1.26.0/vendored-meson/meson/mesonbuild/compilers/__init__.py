# Copyright 2017 The Meson development team

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Public symbols for compilers sub-package when using 'from . import compilers'
__all__ = [
    'Compiler',
    'CompileResult',
    'RunResult',

    'all_languages',
    'base_options',
    'clib_langs',
    'clink_langs',
    'c_suffixes',
    'cpp_suffixes',
    'get_base_compile_args',
    'get_base_link_args',
    'is_assembly',
    'is_header',
    'is_library',
    'is_llvm_ir',
    'is_object',
    'is_source',
    'is_known_suffix',
    'lang_suffixes',
    'LANGUAGES_USING_LDFLAGS',
    'sort_clink',
    'SUFFIX_TO_LANG',

    'compiler_from_language',
    'detect_compiler_for',
    'detect_static_linker',
    'detect_c_compiler',
    'detect_cpp_compiler',
    'detect_cuda_compiler',
    'detect_fortran_compiler',
    'detect_objc_compiler',
    'detect_objcpp_compiler',
    'detect_java_compiler',
    'detect_cs_compiler',
    'detect_vala_compiler',
    'detect_rust_compiler',
    'detect_d_compiler',
    'detect_swift_compiler',
]

# Bring symbols from each module into compilers sub-package namespace
from .compilers import (
    Compiler,
    CompileResult,
    RunResult,
    all_languages,
    base_options,
    clib_langs,
    clink_langs,
    c_suffixes,
    cpp_suffixes,
    get_base_compile_args,
    get_base_link_args,
    is_header,
    is_source,
    is_assembly,
    is_llvm_ir,
    is_object,
    is_library,
    is_known_suffix,
    lang_suffixes,
    LANGUAGES_USING_LDFLAGS,
    sort_clink,
    SUFFIX_TO_LANG,
)
from .detect import (
    compiler_from_language,
    detect_compiler_for,
    detect_static_linker,
    detect_c_compiler,
    detect_cpp_compiler,
    detect_cuda_compiler,
    detect_objc_compiler,
    detect_objcpp_compiler,
    detect_fortran_compiler,
    detect_java_compiler,
    detect_cs_compiler,
    detect_vala_compiler,
    detect_rust_compiler,
    detect_d_compiler,
    detect_swift_compiler,
)
