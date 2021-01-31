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
----------------
**ssh notes**
ssh setting I found:
1. I've already set the password from the laptop for knl so it shouldn't ask for it. it was as easy as copying ~/.ssh/id_rsa.pub from my computer to authorized_key of the ~/.ssh/ in 
2. we can create a ssh tunnel similar tthe remote servero vnc:
   ssh -f -N -L 2222:stampede2.tacc.utexas.edu:2222 haghakha@stampede2.tacc.utexas.edu
3. after creating the tunnel we can use it to transfer the data rsync -auve "ssh -p 2222" api haghakha@localhost:~/
4. we can also use that tunnel also to ssh ssh -p 2222 haghakha@localhost
5. the rsync and ssh through th tunnel don't ask the 2ns authen. key by they still nedd the password. I should find a way to remove the password
--------------

**bit operation**
1. using char for bit, very useful for flag 
```C  
  #include <limits.h>		/* for CHAR_BIT */
  
  #define BITMASK(b) (1 << ((b) % CHAR_BIT))
  #define BITSLOT(b) ((b) / CHAR_BIT)
  #define BITSET(a, b) ((a)[BITSLOT(b)] |= BITMASK(b))
  #define BITCLEAR(a, b) ((a)[BITSLOT(b)] &= ~BITMASK(b))
  #define BITTEST(a, b) ((a)[BITSLOT(b)] & BITMASK(b))
  #define BITNSLOTS(nb) ((nb + CHAR_BIT - 1) / CHAR_BIT)   
``` 

2. useful links:
    * [Bit Twiddling Hacks](http://graphics.stanford.edu/~seander/bithacks.html)
    * [The Aggregate Magic Algorithms](http://aggregate.org/MAGIC/)
    * [The bit twidller](https://bits.stephan-brumme.com/)
    * [Bit Twiddling Hacks](http://graphics.stanford.edu/~seander/bithacks.html)
    * [How do you set, clear, and toggle a single bit?](https://stackoverflow.com/questions/47981/how-do-you-set-clear-and-toggle-a-single-bit)
    
 ----------
**autotools basics**
1) create the following files:
  * NEWS
  * README
  * AUTHORS
  * ChangeLog
2) create configure.ac at project’s root directory. The file must contain, at the very least, the AC_INIT and AC_OUTPUT M4 macros.

      ```make 
      #the 2 following lines are necessary
      AC_INIT([tarball_name], [0.01(version_number)], [developer@email.com])
      AC_OUTPUT

      #ask to create a make file
      AM_INIT_AUTOMAKE

      # name of output file
      AC_CONFIG_FILES([Makefile])

      # for c++ programs, makes sure a C++ compiler is available
      AC_PROG_CXX

      # for c programs, makes sure a C compiler is available
      AC_PROG_CC
      
      # path to one source file in your project, autoconf checks
      AC_CONFIG_SRCDIR([src.c])
      ```
  
3) sometimes configure.ac is not enough and more things needed to be added for the project, so we should create Makefile.am

  * Makefile.am syntax is very similar to the makefile
  * Variables ending in _PROGRAMS: codes to be built.
  * similarly for _SCRIPTS, _DATA, _LIBRARIES
  * bin_PROGRAMS is installed into the bindir, which is user-configurable during compilation.
  * if the output is a script then bin_SCRIPTS = bin/MyApp
  * Automake assumes sources are in src directory, otherwise "subdir-objects" option must be passed:
  
    ```make 
    AUTOMAKE_OPTIONS = foreign subdir-objects
    ```
  * any other Makefile rule can be added in Makefile.am and they will be copied verbatim into the generated Makefile
  
   ----------
**extracting metdadata and organizing pdfs**

1. [calibre](https://calibre-ebook.com/) is very good in extracting metadata and organizing E-book. It also has command line interface([CLI](https://manual.calibre-ebook.com/index.html#the-command-line-interface)) and a [python API](https://pypi.org/project/capybre/). It has a very good function that fetchs data from google or amazon [fetch-ebook-metadata](https://manual.calibre-ebook.com/generated/en/fetch-ebook-metadata.html)

2. [i-librarian](https://i-librarian.net/compare.php) is a browser based pdf manager. It is not great in extracting metadat for ebooks but it's good for papers. It is more a replacement for mendeley. 

3. [CERMINE](https://github.com/CeON/CERMINE) is good in extracting metadata for papers. It has AI features to look for metadata information in a paper. 
  
  
  
  
