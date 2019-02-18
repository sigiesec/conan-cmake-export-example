from conans import ConanFile, CMake

class DependentConan(ConanFile):
    name = "dependent"
    version = "0.1"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Hello here>"
    settings = "os", "compiler", "build_type", "arch"
    options = {}
    default_options = {}
    generators = "cmake"
    exports_sources = "main/*"

    requires = ("base/0.1@foo/bar",)

    def configure_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder="main")
        return cmake

    def build(self):
        cmake = self.configure_cmake()
        cmake.build()

    def package(self):
        #self.copy("*.h", dst="include", src="src")
        #self.copy("*.lib", dst="lib", keep_path=False)
        #self.copy("*.dll", dst="bin", keep_path=False)
        #self.copy("*.dylib*", dst="lib", keep_path=False)
        #self.copy("*.so", dst="lib", keep_path=False)
        #self.copy("*.a", dst="lib", keep_path=False)
        cmake = self.configure_cmake()
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["c"]
