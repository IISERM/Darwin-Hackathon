function readfasta()
    fasta = ""
    open("seq.fasta") do f
        fasta = readlines(f)[2]
    end
    return fasta
end

fasta = readfasta()
k = 5
kmers = []

for i in 1:length(fasta) - k
    # i -> i+k-1 is a kmer starting at i
    push!(kmers, fasta[i:i + k - 1])
end

dict = Dict()

for i in kmers
    # if kmer already in dict, add one, else set to 1
    dict[i] = get(dict, i, 0) + 1
    #                      |---This is a default value
end

# collect the keys--------|                   |--- sort by this function
sortedkeys = sort(collect(keys(dict)), by=kmer -> dict[kmer], rev=true)
#                                                               |-- in reverse order

best = []
for i in sortedkeys
    if length(best) == 0 || dict[i] == dict[best[1]]
        # find all the `best` kmers
        push!(best, i)
    else
        # we have found all. Break
        break
    end
end

# Print stuff

println(length(keys(dict)))
println(best)
println(count(x -> x == best[1], kmers))
