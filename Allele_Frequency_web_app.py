#!/usr/bin/python

from flask import Flask, render_template, request
import math
#from scipy.stats import chisquare
app = Flask(__name__)

@app.route('/')
def student():
   return render_template('HW.html')

@app.route('/HW_result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      ho1 = float(result['ho1'])
      ho2 = float(result['ho2'])
      hetero = float(result['he'])
      n = ho1 + ho2 + hetero
      p = (((ho1 * 2) + (hetero * 1))/(n * 2))
      q = (1 - p)
      standard_error_of_allele_freq = math.sqrt((p * q)/(2 * n))
      pos_CI_p = p + (1.96 * standard_error_of_allele_freq)
      neg_CI_p = p - (1.96 * standard_error_of_allele_freq)
      pos_CI_q = q + (1.96 * standard_error_of_allele_freq)
      neg_CI_q = q - (1.96 * standard_error_of_allele_freq)
      HW = (p * p) + (2 * p * q) + (q * q)
      Expected_P2 = (p * p * n)
      Expected_Q2 = (q * q * n)
      Expected_Heterozygotes = (2 * p * q * n)
      Chi_Square_value = (((ho1 - Expected_P2)**2/Expected_P2)+((ho2 - Expected_Q2)**2/Expected_Q2)+((hetero-Expected_Heterozygotes)**2/Expected_Heterozygotes))
      obs = [ho1,ho2,hetero]
      exp = [Expected_P2,Expected_Q2,Expected_Heterozygotes]
      #chi_test = chisquare(f_obs=obs, f_exp=exp)
      allele_result_dict = {'Allele Frequency of p':p,'Allele Frequency of q':q}
      CI_dict = {'Ninety Five Percent (95%) CI for p': [pos_CI_p,neg_CI_p], 'Ninety Five Percent (95%) CI for q': [pos_CI_q,neg_CI_q]}
      Expected_result_dict = {'Expected Homozygotes(P2)':Expected_P2, 'Expected Homozygotes(Q2)':Expected_Q2, 'Expected Heterozygotes(2PQ)':Expected_Heterozygotes}
      Observed_result_dict = {'Observed Homozygotes(p2)':ho1, 'Observed Homozygotes(q2)':ho2, 'Observed Heterozygotes(2pq)':hetero}
      return render_template("HW_result.html", allele = allele_result_dict, HW = HW, Chi = Chi_Square_value, CI = CI_dict, obs = Observed_result_dict, exp = Expected_result_dict)

if __name__ == '__main__':
   app.run(debug = True)
