# Configuration file for ipython-kernel.

#------------------------------------------------------------------------------
# Configurable configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# LoggingConfigurable configuration
#------------------------------------------------------------------------------

# A parent class for Configurables that log.
#
# Subclasses have a log trait, and the default behavior is to get the logger
# from the currently running Application.

#------------------------------------------------------------------------------
# ConnectionFileMixin configuration
#------------------------------------------------------------------------------

# Mixin for configurable classes that work with connection files

c.InteractiveShellApp.exec_lines = []
c.InteractiveShellApp.exec_lines.append('%load_ext autoreload')
c.InteractiveShellApp.exec_lines.append('%autoreload 2')

#
# c.ConnectionFileMixin.transport = 'tcp'

# set the shell (ROUTER) port [default: random]
# c.ConnectionFileMixin.shell_port = 0

# JSON file in which to store connection info [default: kernel-<pid>.json]
#
# This file will contain the IP, ports, and authentication key needed to connect
# clients to this kernel. By default, this file will be created in the security
# dir of the current profile, but can be specified by absolute path.
# c.ConnectionFileMixin.connection_file = ''

# set the control (ROUTER) port [default: random]
# c.ConnectionFileMixin.control_port = 0

# set the heartbeat port [default: random]
# c.ConnectionFileMixin.hb_port = 0

# set the stdin (ROUTER) port [default: random]
# c.ConnectionFileMixin.stdin_port = 0

# set the iopub (PUB) port [default: random]
# c.ConnectionFileMixin.iopub_port = 0

# Set the kernel's IP address [default localhost]. If the IP address is
# something other than localhost, then Consoles on other machines will be able
# to connect to the Kernel, so be careful!
# c.ConnectionFileMixin.ip = ''

#------------------------------------------------------------------------------
# InteractiveShellApp configuration
#------------------------------------------------------------------------------

# A Mixin for applications that start InteractiveShell instances.
#
# Provides configurables for loading extensions and executing files as part of
# configuring a Shell environment.
#
# The following methods should be called by the :meth:`initialize` method of the
# subclass:
#
#   - :meth:`init_path`
#   - :meth:`init_shell` (to be implemented by the subclass)
#   - :meth:`init_gui_pylab`
#   - :meth:`init_extensions`
#   - :meth:`init_code`

# Should variables loaded at startup (by startup files, exec_lines, etc.) be
# hidden from tools like %who?
# c.InteractiveShellApp.hide_initial_ns = True

# Configure matplotlib for interactive use with the default matplotlib backend.
c.InteractiveShellApp.matplotlib = 'inline'

# Run the module as a script.
# c.InteractiveShellApp.module_to_run = ''

# Pre-load matplotlib and numpy for interactive use, selecting a particular
# matplotlib backend and loop integration.
# c.InteractiveShellApp.pylab = None

# A file to be run
# c.InteractiveShellApp.file_to_run = ''

# A list of dotted module names of IPython extensions to load.
# c.InteractiveShellApp.extensions = traitlets.Undefined

# If true, IPython will populate the user namespace with numpy, pylab, etc. and
# an ``import *`` is done from numpy and pylab, when using pylab mode.
#
# When False, pylab mode should not import any names into the user namespace.
# c.InteractiveShellApp.pylab_import_all = True

# Enable GUI event loop integration with any of ('glut', 'gtk', 'gtk3', 'osx',
# 'pyglet', 'qt', 'qt5', 'tk', 'wx').
# c.InteractiveShellApp.gui = None

# lines of code to run at IPython startup.
# c.InteractiveShellApp.exec_lines = traitlets.Undefined

# dotted module name of an IPython extension to load.
# c.InteractiveShellApp.extra_extension = ''

# Reraise exceptions encountered loading IPython extensions?
# c.InteractiveShellApp.reraise_ipython_extension_failures = False

# Run the file referenced by the PYTHONSTARTUP environment variable at IPython
# startup.
# c.InteractiveShellApp.exec_PYTHONSTARTUP = True

# List of files to run at IPython startup.
# c.InteractiveShellApp.exec_files = traitlets.Undefined

# Execute the given command string.
# c.InteractiveShellApp.code_to_run = ''

#------------------------------------------------------------------------------
# SingletonConfigurable configuration
#------------------------------------------------------------------------------

# A configurable that only allows one instance.
#
# This class is for classes that should only have one instance of itself or
# *any* subclass. To create and retrieve such a class use the
# :meth:`SingletonConfigurable.instance` method.

#------------------------------------------------------------------------------
# Application configuration
#------------------------------------------------------------------------------

# This is an application.

# The Logging format template
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

# Set the log level by value or name.
# c.Application.log_level = 30

# The date format used by logging formatters for %(asctime)s
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

#------------------------------------------------------------------------------
# BaseIPythonApplication configuration
#------------------------------------------------------------------------------

# IPython: an enhanced interactive Python shell.

# Whether to create profile dir if it doesn't exist
# c.BaseIPythonApplication.auto_create = False

# Whether to install the default config files into the profile dir. If a new
# profile is being created, and IPython contains config files for that profile,
# then they will be staged into the new directory.  Otherwise, default config
# files will be automatically generated.
# c.BaseIPythonApplication.copy_config_files = False

# The name of the IPython directory. This directory is used for logging
# configuration (through profiles), history storage, etc. The default is usually
# $HOME/.ipython. This option can also be specified through the environment
# variable IPYTHONDIR.
# c.BaseIPythonApplication.ipython_dir = ''

# The IPython profile to use.
# c.BaseIPythonApplication.profile = 'default'

# Whether to overwrite existing config files when copying
# c.BaseIPythonApplication.overwrite = False

# Create a massive crash report when IPython encounters what may be an internal
# error.  The default is to append a short message to the usual traceback
# c.BaseIPythonApplication.verbose_crash = False

# Path to an extra config file to load.
#
# If specified, load this config file in addition to any other IPython config.
# c.BaseIPythonApplication.extra_config_file = ''

#------------------------------------------------------------------------------
# IPKernelApp configuration
#------------------------------------------------------------------------------

# IPython: an enhanced interactive Python shell.

# ONLY USED ON WINDOWS Interrupt this process when the parent is signaled.
# c.IPKernelApp.interrupt = 0

# redirect stderr to the null device
# c.IPKernelApp.no_stderr = False

# The importstring for the OutStream factory
# c.IPKernelApp.outstream_class = 'ipykernel.iostream.OutStream'

# redirect stdout to the null device
# c.IPKernelApp.no_stdout = False

# The Kernel subclass to be used.
#
# This should allow easy re-use of the IPKernelApp entry point to configure and
# launch kernels other than IPython's own.
# c.IPKernelApp.kernel_class = <class 'ipykernel.ipkernel.IPythonKernel'>

# The importstring for the DisplayHook factory
# c.IPKernelApp.displayhook_class = 'ipykernel.displayhook.ZMQDisplayHook'

# kill this process if its parent dies.  On Windows, the argument specifies the
# HANDLE of the parent process, otherwise it is simply boolean.
# c.IPKernelApp.parent_handle = 0

#------------------------------------------------------------------------------
# Kernel configuration
#------------------------------------------------------------------------------

#
# c.Kernel._execute_sleep = 0.0005

#
# c.Kernel._poll_interval = 0.05

# Whether to use appnope for compatiblity with OS X App Nap.
#
# Only affects OS X >= 10.9.
# c.Kernel._darwin_app_nap = True

#------------------------------------------------------------------------------
# IPythonKernel configuration
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
# InteractiveShell configuration
#------------------------------------------------------------------------------

# An enhanced, interactive shell for Python.

# Use colors for displaying information about objects. Because this information
# is passed through a pager (like 'less'), and some pagers get confused with
# color codes, this capability can be turned off.
# c.InteractiveShell.color_info = True

# Start logging to the given file in append mode. Use `logfile` to specify a log
# file to **overwrite** logs to.
# c.InteractiveShell.logappend = ''

#
# c.InteractiveShell.quiet = False

# The number of saved history entries to be loaded into the readline buffer at
# startup.
# c.InteractiveShell.history_load_length = 1000

#
# c.InteractiveShell.ipython_dir = ''

#
# c.InteractiveShell.object_info_string_level = 0

# The part of the banner to be printed after the profile
# c.InteractiveShell.banner2 = ''

# Set the size of the output cache.  The default is 1000, you can change it
# permanently in your config file.  Setting it to 0 completely disables the
# caching system, and the minimum value accepted is 20 (if you provide a value
# less than 20, it is reset to 0 and a warning is issued).  This limit is
# defined because otherwise you'll spend more time re-flushing a too small cache
# than working
# c.InteractiveShell.cache_size = 1000

#
# c.InteractiveShell.history_length = 10000

#
# c.InteractiveShell.separate_out2 = ''

# Don't call post-execute functions that have failed in the past.
# c.InteractiveShell.disable_failing_post_execute = False

# Save multi-line entries as one entry in readline history
# c.InteractiveShell.multiline_history = True

# Make IPython automatically call any callable object even if you didn't type
# explicit parentheses. For example, 'str 43' becomes 'str(43)' automatically.
# The value can be '0' to disable the feature, '1' for 'smart' autocall, where
# it is not applied if there are no more arguments on the line, and '2' for
# 'full' autocall, where all callable objects are automatically called (even if
# no arguments are present).
# c.InteractiveShell.autocall = 0

# Set the color scheme (NoColor, Linux, or LightBG).
# c.InteractiveShell.colors = 'LightBG'

#
# c.InteractiveShell.debug = False

# A list of ast.NodeTransformer subclass instances, which will be applied to
# user input before code is run.
# c.InteractiveShell.ast_transformers = traitlets.Undefined

#
# c.InteractiveShell.readline_use = True

# **Deprecated**
#
# Enable deep (recursive) reloading by default. IPython can use the deep_reload
# module which reloads changes in modules recursively (it replaces the reload()
# function, so you don't need to change anything to use it). `deep_reload`
# forces a full reload of modules whose code may have changed, which the default
# reload() function does not.  When deep_reload is off, IPython will use the
# normal reload(), but deep_reload will still be available as dreload().
# c.InteractiveShell.deep_reload = False

# Deprecated, use PromptManager.in_template
# c.InteractiveShell.prompt_in1 = 'In [\\#]: '

# 'all', 'last', 'last_expr' or 'none', specifying which nodes should be run
# interactively (displaying output from expressions).
# c.InteractiveShell.ast_node_interactivity = 'last_expr'

#
# c.InteractiveShell.separate_in = '\n'

# Start logging to the default log file in overwrite mode. Use `logappend` to
# specify a log file to **append** logs to.
# c.InteractiveShell.logstart = False

# Deprecated, use PromptManager.in2_template
# c.InteractiveShell.prompt_in2 = '   .\\D.: '

# The part of the banner to be printed before the profile
# c.InteractiveShell.banner1 = 'Python 3.5.1 (default, Dec  7 2015, 21:59:10) \nType "copyright", "credits" or "license" for more information.\n\nIPython 4.0.1 -- An enhanced Interactive Python.\n?         -> Introduction and overview of IPython\'s features.\n%quickref -> Quick reference.\nhelp      -> Python\'s own help system.\nobject?   -> Details about \'object\', use \'object??\' for extra details.\n'

# If True, anything that would be passed to the pager will be displayed as
# regular output instead.
# c.InteractiveShell.display_page = False

# Enable magic commands to be called without the leading %.
# c.InteractiveShell.automagic = True

#
# c.InteractiveShell.readline_remove_delims = '-/~'

# Show rewritten input, e.g. for autocall.
# c.InteractiveShell.show_rewritten_input = True

#
# c.InteractiveShell.separate_out = ''

# The name of the logfile to use.
# c.InteractiveShell.logfile = ''

#
# c.InteractiveShell.readline_parse_and_bind = traitlets.Undefined

#
# c.InteractiveShell.wildcards_case_sensitive = True

# Deprecated, use PromptManager.justify
# c.InteractiveShell.prompts_pad_left = True

# Autoindent IPython code entered interactively.
# c.InteractiveShell.autoindent = True

#
# c.InteractiveShell.xmode = 'Context'

# Automatically call the pdb debugger after every exception.
# c.InteractiveShell.pdb = False

# Deprecated, use PromptManager.out_template
# c.InteractiveShell.prompt_out = 'Out[\\#]: '

#------------------------------------------------------------------------------
# ZMQInteractiveShell configuration
#------------------------------------------------------------------------------

# A subclass of InteractiveShell for ZMQ.

#------------------------------------------------------------------------------
# ProfileDir configuration
#------------------------------------------------------------------------------

# An object to manage the profile directory and its resources.
#
# The profile directory is used by all IPython applications, to manage
# configuration, logging and security.
#
# This object knows how to find, create and manage these directories. This
# should be used by any code that wants to handle profiles.

# Set the profile location directly. This overrides the logic used by the
# `profile` option.
# c.ProfileDir.location = ''

#------------------------------------------------------------------------------
# Session configuration
#------------------------------------------------------------------------------

# Object for handling serialization and sending of messages.
#
# The Session object handles building messages and sending them with ZMQ sockets
# or ZMQStream objects.  Objects can communicate with each other over the
# network via Session objects, and only need to work with the dict-based IPython
# message spec. The Session will handle serialization/deserialization, security,
# and metadata.
#
# Sessions support configurable serialization via packer/unpacker traits, and
# signing with HMAC digests via the key/keyfile traits.
#
# Parameters ----------
#
# debug : bool
#     whether to trigger extra debugging statements
# packer/unpacker : str : 'json', 'pickle' or import_string
#     importstrings for methods to serialize message parts.  If just
#     'json' or 'pickle', predefined JSON and pickle packers will be used.
#     Otherwise, the entire importstring must be used.
#
#     The functions must accept at least valid JSON input, and output *bytes*.
#
#     For example, to use msgpack:
#     packer = 'msgpack.packb', unpacker='msgpack.unpackb'
# pack/unpack : callables
#     You can also set the pack/unpack callables for serialization directly.
# session : bytes
#     the ID of this Session object.  The default is to generate a new UUID.
# username : unicode
#     username added to message headers.  The default is to ask the OS.
# key : bytes
#     The key used to initialize an HMAC signature.  If unset, messages
#     will not be signed or checked.
# keyfile : filepath
#     The file containing a key.  If this is set, `key` will be initialized
#     to the contents of the file.

# execution key, for signing messages.
# c.Session.key = b''

# The name of the unpacker for unserializing messages. Only used with custom
# functions for `packer`.
# c.Session.unpacker = 'json'

# path to file containing execution key.
# c.Session.keyfile = ''

# Username for the Session. Default is your system username.
# c.Session.username = 'dgolden'

# Threshold (in bytes) beyond which an object's buffer should be extracted to
# avoid pickling.
# c.Session.buffer_threshold = 1024

# The digest scheme used to construct the message signatures. Must have the form
# 'hmac-HASH'.
# c.Session.signature_scheme = 'hmac-sha256'

# The maximum number of digests to remember.
#
# The digest history will be culled when it exceeds this value.
# c.Session.digest_history_size = 65536

# The UUID identifying this session.
# c.Session.session = ''

# Debug output in the Session
# c.Session.debug = False

# The name of the packer for serializing messages. Should be one of 'json',
# 'pickle', or an import name for a custom callable serializer.
# c.Session.packer = 'json'

# The maximum number of items for a container to be introspected for custom
# serialization. Containers larger than this are pickled outright.
# c.Session.item_threshold = 64

# Threshold (in bytes) beyond which a buffer should be sent without copying.
# c.Session.copy_threshold = 65536

# Metadata dictionary, which serves as the default top-level metadata dict for
# each message.
# c.Session.metadata = traitlets.Undefined

# Subset of matplotlib rcParams that should be different for the inline backend.
c.InlineBackend.rc = {'font.size': 14, 'figure.figsize': (8.0, 5.5), 'figure.facecolor': 'white', 'savefig.dpi': 72, 'figure.subplot.bottom': 0.125, 'figure.edgecolor': 'white'}
