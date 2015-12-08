% Interaction plot

clear all
close all
clc

load ghd_climate_data_20th_century.mat

mdl = fitlm(temp_prec_pdsi_1901_1980(:,[1 2]),ghdcore_1901_1980);

mdl

figure
plotInteraction(mdl,'x1','x2','effects')

mdl = fitlm(temp_prec_pdsi_1981_2007(:,[1 2]),ghdcore_1981_2007);

mdl

figure
plotInteraction(mdl,'x1','x2','effects')

return

% PDSI

mdl = fitlm(temp_prec_pdsi_1901_1980(:,[1 3]),ghdcore_1901_1980);

mdl

figure
plotInteraction(mdl,'x1','x2')

mdl = fitlm(temp_prec_pdsi_1981_2007(:,[1 3]),ghdcore_1981_2007);

mdl

figure
plotInteraction(mdl,'x1','x2')
