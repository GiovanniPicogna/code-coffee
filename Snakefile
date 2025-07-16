rule simulation:
    output:
        "src/data/data{group}.hdf5"
    conda:
        "environment.yml"
    cache:
        True
    params:
        v_frag = 1.,
        rho_dust = 2.,
        alpha = 5.e-4,
        stellar_mass = 0.1,
        dust_to_gas_ratio = 0.01,
        disk_mass = 0.1
    script:
        "src/scripts/simulation.py"
