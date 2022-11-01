(base) raccoononion@Ryans-MacBook-Air sample % sh experiment.sh -fpl
Dataset: out.cit-HepPh, dataset type: 0.75, ind
Results: a=3688.433934542118, b=-0.8808545529616448; stdev of a: 71.84042319372766, stdev of b: 0.01446590592683887
Dataset: out.cit-HepPh, dataset type: original, ind
Results: a=4874.252553624073, b=-0.8918560945414666; stdev of a: 86.50127684808344, stdev of b: 0.01338338574302494
Dataset: out.cit-HepPh, dataset type: 0.75, outd
Results: a=2796.369919228415, b=-0.707578248390729; stdev of a: 144.1565664296835, stdev of b: 0.027578893017761973
Dataset: out.cit-HepPh, dataset type: original, outd
Results: a=3662.847929115547, b=-0.7135707724410261; stdev of a: 180.7448050099134, stdev of b: 0.026481949975836243
------------------------------------------------------------------------------------------------------------------------------------------
Dataset: out.citeseer, dataset type: 0.75, ind
Results: a=41710.42677056991, b=-1.1042964838994782; stdev of a: 367.14217182683694, stdev of b: 0.010283361218419136
Dataset: out.citeseer, dataset type: original, ind
Results: a=55602.0742056481, b=-1.1060745355620278; stdev of a: 449.72437347314826, stdev of b: 0.009460058420792828
Dataset: out.citeseer, dataset type: 0.75, outd
Results: a=62504.61725176428, b=-0.9638013052852517; stdev of a: 2165.0005041532154, stdev of b: 0.03195519979953249
Dataset: out.citeseer, dataset type: original, outd
Results: a=83365.02699808226, b=-0.9682338363396602; stdev of a: 2705.623039939354, stdev of b: 0.0299202293924888
------------------------------------------------------------------------------------------------------------------------------------------
Dataset: out.dblp-cite, dataset type: 0.75, ind
Results: a=4031.029063996054, b=-1.5081932928818436; stdev of a: 15.204321986624153, stdev of b: 0.008587255371451446
Dataset: out.dblp-cite, dataset type: original, ind
Results: a=5366.22839612928, b=-1.5214878383184525; stdev of a: 17.8638295779711, stdev of b: 0.007711460512520279
Dataset: out.dblp-cite, dataset type: 0.75, outd
Results: a=148.75016883649047, b=-0.4370716400269038; stdev of a: 25.566795732944925, stdev of b: 0.06782272219844582
Dataset: out.dblp-cite, dataset type: original, outd
Results: a=188.55135952761546, b=-0.4536627105363609; stdev of a: 30.467982646767194, stdev of b: 0.06318253231197897
------------------------------------------------------------------------------------------------------------------------------------------
Dataset: out.librec-ciaodvd-trust, dataset type: 0.75, ind
Results: a=1377.8197069915725, b=-1.5168666144845273; stdev of a: 4.31875143212679, stdev of b: 0.007201556428806195
Dataset: out.librec-ciaodvd-trust, dataset type: original, ind
Results: a=1813.3378922074442, b=-1.5660460295922995; stdev of a: 5.0938344829577895, stdev of b: 0.006889867108071625
Dataset: out.librec-ciaodvd-trust, dataset type: 0.75, outd
Results: a=141.49327615469335, b=-0.7370019019289583; stdev of a: 3.6623831349465537, stdev of b: 0.01583585385577292
Dataset: out.librec-ciaodvd-trust, dataset type: original, outd
Results: a=190.20350391305112, b=-0.8386352981983779; stdev of a: 3.6509718329941236, stdev of b: 0.01391136660643296
------------------------------------------------------------------------------------------------------------------------------------------
Dataset: out.librec-filmtrust-trust, dataset type: 0.75, ind
Results: a=327.4031771057202, b=-1.808678563775206; stdev of a: 2.358416110876499, stdev of b: 0.024067621127317803
Dataset: out.librec-filmtrust-trust, dataset type: original, ind
Results: a=434.4590919690736, b=-1.8755880899292559; stdev of a: 2.6092785942362, stdev of b: 0.0215496161861444
Dataset: out.librec-filmtrust-trust, dataset type: 0.75, outd
Results: a=221.34588390872437, b=-1.426634707954648; stdev of a: 6.04507573086934, stdev of b: 0.05750134162300909
Dataset: out.librec-filmtrust-trust, dataset type: original, outd
Results: a=294.21335215922403, b=-1.4793589515515229; stdev of a: 6.623168682408502, stdev of b: 0.05034364481639983
------------------------------------------------------------------------------------------------------------------------------------------
Dataset: out.munmun_twitter_social, dataset type: 0.75, ind
Results: a=265021.05609102885, b=-2.5862934198911347; stdev of a: 36.289599430252586, stdev of b: 0.000977156756240215
Dataset: out.munmun_twitter_social, dataset type: original, ind
Results: a=353292.3621319519, b=-2.587206027072015; stdev of a: 46.234916479568774, stdev of b: 0.0009346435563258815
Dataset: out.munmun_twitter_social, dataset type: 0.75, outd
Results: a=5.8647717559649664e-09, b=3.4647264130479485; stdev of a: 1.1956829070741038e-08, stdev of b: 0.33357494474815746
Traceback (most recent call last):
  File "/Users/raccoononion/git-repos/sample/results/out.munmun_twitter_social/../../src/fit-pl.py", line 26, in <module>
    pars, cov = curve_fit(f=power_law, xdata=deg_list_ad, ydata=fre_list_ad, p0=[0, 0], bounds=(-np.inf, np.inf))
  File "/Users/raccoononion/opt/anaconda3/lib/python3.9/site-packages/scipy/optimize/_minpack_py.py", line 839, in curve_fit
    raise RuntimeError("Optimal parameters not found: " + errmsg)
RuntimeError: Optimal parameters not found: Number of calls to function has reached maxfev = 600.
------------------------------------------------------------------------------------------------------------------------------------------
Dataset: out.soc-Epinions1, dataset type: 0.75, ind
Results: a=18048.0199891295, b=-1.598672570698847; stdev of a: 7.842102670513927, stdev of b: 0.0011114458432175867
Dataset: out.soc-Epinions1, dataset type: original, ind
Results: a=24066.00936098144, b=-1.6116980039717195; stdev of a: 13.105570686972472, stdev of b: 0.001416566838126782
Dataset: out.soc-Epinions1, dataset type: 0.75, outd
Results: a=21855.607030479343, b=-1.6969862378722893; stdev of a: 21.39735086877601, stdev of b: 0.00283466417427583
Dataset: out.soc-Epinions1, dataset type: original, outd
Results: a=29149.37291109052, b=-1.705147628828134; stdev of a: 19.46313146804848, stdev of b: 0.0019525449592511222
------------------------------------------------------------------------------------------------------------------------------------------
Dataset: out.youtube-links, dataset type: 0.75, ind
Results: a=508551.691639768, b=-1.9600925230598365; stdev of a: 98.71377732283865, stdev of b: 0.0007588711897857718
Dataset: out.youtube-links, dataset type: original, ind
Results: a=678075.2628195599, b=-1.9605194702832196; stdev of a: 125.49661291720138, stdev of b: 0.0007238985607091987
Dataset: out.youtube-links, dataset type: 0.75, outd
Results: a=144682.56392851425, b=-1.1981593181465868; stdev of a: 810.7868708630646, stdev of b: 0.007775536066905102
Dataset: out.youtube-links, dataset type: original, outd
Results: a=192927.26373380443, b=-1.1988747020099204; stdev of a: 1010.2078707500316, stdev of b: 0.0072712941013031735
------------------------------------------------------------------------------------------------------------------------------------------
Power Law fitting finished!
Current directory is: /Users/raccoononion/git-repos/sample/results