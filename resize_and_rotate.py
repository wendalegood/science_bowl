import os
root = '/home/ecater/Desktop/competition_data/train'
y = """acantharia_protist_big_center	acantharia_protist_halo	acantharia_protist	amphipods	appendicularian_fritillaridae	appendicularian_s_shape	appendicularian_slight_curve	appendicularian_straight	artifacts_edge	artifacts	chaetognath_non_sagitta	chaetognath_other	chaetognath_sagitta	chordate_type1	copepod_calanoid_eggs	copepod_calanoid_eucalanus	copepod_calanoid_flatheads	copepod_calanoid_frillyAntennae	copepod_calanoid_large_side_antennatucked	copepod_calanoid_large	copepod_calanoid_octomoms	copepod_calanoid_small_longantennae	copepod_calanoid	copepod_cyclopoid_copilia	copepod_cyclopoid_oithona_eggs	copepod_cyclopoid_oithona	copepod_other	crustacean_other	ctenophore_cestid	ctenophore_cydippid_no_tentacles	ctenophore_cydippid_tentacles	ctenophore_lobate	decapods	detritus_blob	detritus_filamentous	detritus_other	diatom_chain_string	diatom_chain_tube	echinoderm_larva_pluteus_brittlestar	echinoderm_larva_pluteus_early	echinoderm_larva_pluteus_typeC	echinoderm_larva_pluteus_urchin	echinoderm_larva_seastar_bipinnaria	echinoderm_larva_seastar_brachiolaria	echinoderm_seacucumber_auricularia_larva	echinopluteus	ephyra	euphausiids_young	euphausiids	fecal_pellet	fish_larvae_deep_body	fish_larvae_leptocephali	fish_larvae_medium_body	fish_larvae_myctophids	fish_larvae_thin_body	fish_larvae_very_thin_body	heteropod	hydromedusae_aglaura	hydromedusae_bell_and_tentacles	hydromedusae_h15	hydromedusae_haliscera_small_sideview	hydromedusae_haliscera	hydromedusae_liriope	hydromedusae_narco_dark	hydromedusae_narco_young	hydromedusae_narcomedusae	hydromedusae_other	hydromedusae_partial_dark	hydromedusae_shapeA_sideview_small	hydromedusae_shapeA	hydromedusae_shapeB	hydromedusae_sideview_big	hydromedusae_solmaris	hydromedusae_solmundella	hydromedusae_typeD_bell_and_tentacles	hydromedusae_typeD	hydromedusae_typeE	hydromedusae_typeF	invertebrate_larvae_other_A	invertebrate_larvae_other_B	jellies_tentacles	polychaete	protist_dark_center	protist_fuzzy_olive	protist_noctiluca	protist_other	protist_star	pteropod_butterfly	pteropod_theco_dev_seq	pteropod_triangle	radiolarian_chain	radiolarian_colony	shrimp_caridean	shrimp_sergestidae	shrimp_zoea	shrimp-like_other	siphonophore_calycophoran_abylidae	siphonophore_calycophoran_rocketship_adult	siphonophore_calycophoran_rocketship_young	siphonophore_calycophoran_sphaeronectes_stem	siphonophore_calycophoran_sphaeronectes_young	siphonophore_calycophoran_sphaeronectes	siphonophore_other_parts	siphonophore_partial	siphonophore_physonect_young	siphonophore_physonect	stomatopod	tornaria_acorn_worm_larvae	trichodesmium_bowtie	trichodesmium_multiple	trichodesmium_puff	trichodesmium_tuft	trochophore_larvae	tunicate_doliolid_nurse	tunicate_doliolid	tunicate_partial	tunicate_salp_chains	tunicate_salp	unknown_blobs_and_smudges	unknown_sticks	unknown_unclassified """
# convert chaetognath_non_sagitta/53.jpg -rotate 90 -resize 200x200! howtogeek-rotated.jpg


folders = y.split() 
"""
for i in range(len(folders)):
    for fileNameDir in os.walk(root + '/' + folders[i]):
        for fileName in fileNameDir[2]:
            if fileName[-4:] != ".jpg":
                continue
	    os.system("convert %s -resize 96x96! %s" % (folders[i] + '/' + fileName, folders[i] + '/' + fileName))
	    """

for i in range(len(folders)):
    for fileNameDir in os.walk(root + '/' + folders[i]):
        for fileName in fileNameDir[2]:
            if fileName[-4:] != ".jpg":
                continue
	    for j in range(0, 360, 36):
		#if j == 0:
	    #os.system("convert %s -resize 96x96! %s" % (folders[i] + '/' + fileName, folders[i] + '/' + fileName))
	    #print "convert %s -resize 96x96! %s" % (folders[i] + '/' + fileName, folders[i] + '/' + fileName)
		os.system("convert %s -rotate %s -resize 96x96! %s" % (folders[i] + '/' + fileName, str(j), folders[i] + '/' + fileName[:-4] + '-' + str(j) + '.jpg' ))