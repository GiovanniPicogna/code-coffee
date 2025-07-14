from dustpy import Simulation, constants
import paths

sim = Simulation()
sim.initialize()

sim.dust.v.frag = snakemake.params["v_frag"]
sim.dust.rhos = snakemake.params["rho_dust"]
sim.gas.alpha = snakemake.params["alpha"]
sim.star.M = snakemake.params["stellar_mass"]*constants.M_sun
sim.dust.eps = snakemake.params["dust_to_gas_ratio"]
sim.gas.Mdisk = snakemake.params["disk_mass"]*constants.M_sun

sim.writer.datadir = paths.data
sim.writer.overwrite = True

sim.run()
