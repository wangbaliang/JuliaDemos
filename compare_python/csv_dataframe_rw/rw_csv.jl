
using Dates
using CSV
using DataFrames

path_log = joinpath(dirname(@__FILE__), "_DATA_USE")
open(path_log, "r") do io
    global file_path = strip(read(io, String))
    file_path = joinpath(dirname(@__FILE__), file_path)
end

write_path = joinpath(dirname(@__FILE__), "test_w.csv")


println("filepath: $file_path\n")
println("start read csv =========")
@time df = CSV.read(file_path)

println("\nstart write csv =========")

@time CSV.write(write_path, df)
rm(write_path)
