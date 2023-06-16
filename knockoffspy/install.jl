using Pkg
Pkg.add("Knockoffs")
Pkg.add("PyCall")
Pkg.build("PyCall")
using Knockoffs
using PyCall