function Simulation(size,rnot,alpha,u,Model)
    n = 200
    Farm = go(size,rnot)
    dir = 0
    hgt = length(Farm)/2
    hgt = Int(hgt)
    col = 20*ones(hgt,1)
    Farm = hcat(Farm,col)
    Farmn = zeros(hgt,3)
    totVelocity = zeros(1,n)
    #toVelocity = zeros(1,n)
    n2 = 50/n
    for i = 1:n
        Farmn = rotation_matrix(dir,Farm,hgt)
        Farmn = Farmn[sortperm(Farmn[:, 2],rev=true), :]
        wtVelocity = zeros(1,hgt)
        #wVelocity = zeros(1,hgt)
        for j =1:hgt
            if j == 1
                wtVelocity[j] = u
                #wVelocity[j] = u
            elseif j == 2
                wtVelocity[j] = Jensen_Point(alpha, rnot, u, Farmn[j-1,:], Farmn[j,:], Model)
                #wVelocity[j] = Jensen_Point(alpha, rnot, u, Farmn[j-1,:], Farmn[j,:], Model)
            else
                wtVelocity[j] = Katic(Farmn[1:j-1,:], rnot, Farmn[j,:], alpha, u, Model)
                #wVelocity[j] = Katicov(Farmn[1:j-1,:], rnot, Farmn[j,:], alpha, u, Model)
            end
        end
        wtVelocity = wtVelocity.^3
        totVelocity[i] = sum(wtVelocity)
        #toVelocity[i] = sum(wVelocity)
        dir = dir+n2
    end

    return totVelocity
end
