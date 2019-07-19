from conans import ConanFile, CMake, tools

class PodofoConan(ConanFile):
    name = "PoDoFo"
    version = "0.9.6"
    license = "LGPL"
    author = "raulh39"
    url = "https://github.com/raulh39/conan-podofo"
    description = "PoDoFo is a library to work with the PDF file format"
    topics = ("pdf")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = "shared=False"
    generators = "cmake"

    def requirements(self):
        self.requires("libjpeg-turbo/1.5.2@bincrafters/stable")
        self.requires("libtiff/4.0.9@bincrafters/stable")
        self.requires("fontconfig/2.13.91@conan/stable")
        self.requires("OpenSSL/1.1.1d@conan/stable")

    def source(self):
        url = "http://sourceforge.net/projects/podofo/files/podofo/{version}/podofo-{version}.tar.gz"
        tools.get(url.format(version=self.version))
                    
    def build(self):
        folder_name = "podofo-%s" % self.version
        replace_lines = '''PROJECT(PoDoFo CXX)
        
enable_language(C)        
include(../conanbuildinfo.cmake)
conan_basic_setup()
'''
        tools.replace_in_file("%s/CMakeLists.txt" % folder_name, "PROJECT(PoDoFo)", replace_lines)
        self.cmake = CMake(self)
        self.cmake.definitions["PODOFO_BUILD_LIB_ONLY"] = True
        self.cmake.configure(source_folder=folder_name)
        self.cmake.configure(defs={'PODOFO_BUILD_SHARED:BOOL': 'TRUE' if self.options.shared else 'FALSE',
                              'PODOFO_BUILD_STATIC:BOOL': 'FALSE' if self.options.shared else 'TRUE',
                              })
        self.cmake.build()

    def package(self):
        self.cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["podofo"]
