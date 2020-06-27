**dark them eclipse problems and fixed**

  1) occurrences: Open Window>Preferences>General>Editors>Text Editors>Annotations change C/C++ ccurrences color
  2) inactive codes: Open Window>Preferences>C/C++>Editor>change inactive code highlight color

-------------------
**command line and input file parser**

  1) [dropt](https://github.com/jamesderlin/dropt)
  2) [Boost.Program_options](https://www.boost.org/doc/libs/1_58_0/doc/html/program_options.html)
  3) [getopt](https://www.gnu.org/savannah-checkouts/gnu/libc/manual/html_node/Getopt.html)
  4) [Templatized C++ Command Line Parser](https://sourceforge.net/projects/tclap/)
  5) [gflags (formerly Google Commandline Flags)](http://gflags.github.io/gflags/)
  6) [klib](http://attractivechaos.github.io/klib/#About)
  7) [Glib](https://gitlab.gnome.org/GNOME/glib)--> this library is a massive library with many other options including design interface
  8) [clipp](https://github.com/muellan/clipp)
  
  the first option seems the best

a better appraoch is to use some parser generators for the input arguments such as using:
1) [GNU Gengetopt](https://www.gnu.org/software/gengetopt/gengetopt.html)
2) [Autogen](https://www.gnu.org/software/autogen/manual/html_node/autogen.html#Top) and its related section [AutoOpt](https://www.gnu.org/software/autogen/manual/html_node/Features.html#Features)
3) [genparse](https://sourceforge.net/projects/genparse/files/) or [man page](http://manpages.ubuntu.com/manpages/focal/man1/genparse.1.html)

a comparison between them can be found [here](https://www.gnu.org/software/autogen/compare.html)
