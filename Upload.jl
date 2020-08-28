using XLSX
Cos_6x = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "Cos 6", "A1:A56")
Cos_6y = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "Cos 6", "B1:B56")
Cos_10x = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "Cos 10", "A1:A44")
Cos_10y = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "Cos 10", "B1:B44")
Cos_16x = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "Cos 16", "A1:A42")
Cos_16y = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "Cos 16", "B1:B42")
TH_6x = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "TH 6", "A1:A7")
TH_6y = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "TH 6", "B1:B7")
TH_10x = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "TH 10", "A1:A7")
TH_10y = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "TH 10", "B1:B7")
TH_16x = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "TH 16", "A1:A7")
TH_16y = XLSX.readdata("C:\\Users\\Owner\\Documents\\Fall_2019\\495R\\Digitizer_Data.xlsx", "TH 16", "B1:B7")
# Katicx = XLSX.readdata("C:\\Users\\Owner\\Documents\\Research\\Katic_Data.xlsx", "Katic_Data", "A1:A48")
# Katicy = XLSX.readdata("C:\\Users\\Owner\\Documents\\Research\\Katic_Data.xlsx", "Katic_Data", "B1:B48")
# plot!(Katicx[:,1], Katicy[:,1])
# plot!(dir,x)

alpha = .1
rnot = 20
u = 8.1

Turbine1 = [0,0,20]
PosWind1 = [-50,120,20]
PosWind2 = [-100,200,20]
PosWind3 = [-150,320,20]
Model = "Cos"
include("Jensen.jl")
vc6 = zeros(1,100)
thetac6 = zeros(1,100)
vc10 = zeros(1,100)
thetac10 = zeros(1,100)
vc16 = zeros(1,100)
thetac16 = zeros(1,100)

for i = 1:100
    vc6[i] = Jensen_Point(alpha, rnot, u, Turbine1, PosWind1, Model)
    thetac6[i] = atand(Turbine1[1]+PosWind1[1]/PosWind1[2])
    vc10[i] = Jensen_Point(alpha, rnot, u, Turbine1, PosWind2, Model)
    thetac10[i] = atand(Turbine1[1]+PosWind2[1]/PosWind2[2])
    vc16[i] = Jensen_Point(alpha, rnot, u, Turbine1, PosWind3, Model)
    thetac16[i] = atand(Turbine1[1]+PosWind3[1]/PosWind3[2])
    PosWind1[1] += 1
    PosWind2[1] += 2
    PosWind3[1] += 3
end

Model = "TH"
PosWind1 = [-40,120,20]
PosWind2 = [-40,200,20]
PosWind3 = [-40,320,20]
vth6 = zeros(1,80)
thetath6 = zeros(1,80)
vth10 = zeros(1,80)
thetath10 = zeros(1,80)
vth16 = zeros(1,80)
thetath16 = zeros(1,80)

for i = 1:80
    vth6[i] = Jensen_Point(alpha, rnot, u, Turbine1, PosWind1, Model)
    thetath6[i] = atand(Turbine1[1]+PosWind1[1]/PosWind1[2])
    vth10[i] = Jensen_Point(alpha, rnot, u, Turbine1, PosWind2, Model)
    thetath10[i] = atand(Turbine1[1]+PosWind2[1]/PosWind2[2])
    vth16[i] = Jensen_Point(alpha, rnot, u, Turbine1, PosWind3, Model)
    thetath16[i] = atand(Turbine1[1]+PosWind3[1]/PosWind3[2])
    PosWind1[1] += 1
    PosWind2[1] += 1
    PosWind3[1] += 1
end

c6 = plot(thetac6',vc6'./u, legend = false)
c6 = plot!(Cos_6x[:,1], Cos_6y[:,1], ylabel = "v/u", legend = false, title = "Cosine at x/r0=6", xaxis=false)
c10 = plot(thetac10',vc10'./u, legend = false)
c10 = plot!(Cos_10x[:,1], Cos_10y[:,1], ylabel = "v/u", legend = false, title = "Cosine at x/r0=10", xaxis=false)
c16 = plot(thetac16',vc16'./u)
c16 = plot!(Cos_16x[:,1], Cos_16y[:,1], xlabel = "Δθ Degrees", ylabel = "v/u", legend = false, title = "Cosine at x/r0=16")
th6 = plot(thetath6',vth6'./u, legend = false)
th6 = plot!(TH_6x[:,1], TH_6y[:,1], ylabel = "v/u", legend = false, title = "Top Hat at x/r0=6", xaxis=false)
th10 = plot(thetath10',vth10'./u, legend = false)
th10 = plot!(TH_10x[:,1], TH_10y[:,1], ylabel = "v/u", legend = false, title = "Top Hat at x/r0=10", xaxis=false)
th16 = plot(thetath16',vth16'./u)
th16 = plot!(TH_16x[:,1], TH_16y[:,1], xlabel = "Δθ Degrees", ylabel = "v/u",legend = false, title = "Top Hat at x/r0=16")
legend = plot([0 0], showaxis = false, grid = false, label = ["My Code" "Paper Data"])
plot(c6,c10,c16,legend, layout = @layout([[A; B; C] D{.1w}]), link=:x, foreground_color_legend=nothing)
plot(th6,th10,th16,legend, layout = @layout([[A; B; C] D{.1w}]),foreground_color_legend = nothing,background_color = :transparent)
plot(c6,th6,c10,th10,c16,th16,legend, layout = @layout([[A B; C D; E F] G{.1w}]))
plot!(ylims=(.7, 1))
savefig("C:\\Users\\Owner\\Documents\\Research\\Tophat.pdf")
plot!(title = "Jensen Verification", grid = false, showaxis = false, bottom_margin = -50Plots.px)
