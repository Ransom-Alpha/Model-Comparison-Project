import pandas as pd

def capm(beta, risk_free_rate, market_return):
    return risk_free_rate + beta.mul(market_return - risk_free_rate, axis=0)

def black_capm(beta, market_return):
    return beta.mul(market_return, axis=0)

def fama_french_3f(beta_m, beta_smb, beta_hml, risk_free_rate, market_return, smb, hml):
    return (risk_free_rate + beta_m.mul(market_return - risk_free_rate, axis=0) +
            beta_smb.mul(smb, axis=0) + beta_hml.mul(hml, axis=0))

def carhart_4f(beta_m, beta_smb, beta_hml, beta_umd, risk_free_rate, market_return, smb, hml, umd):
    return (risk_free_rate + beta_m.mul(market_return - risk_free_rate, axis=0) +
            beta_smb.mul(smb, axis=0) + beta_hml.mul(hml, axis=0) + beta_umd.mul(umd, axis=0))

def fama_french_5f(beta_m, beta_smb, beta_hml, beta_rmw, beta_cma, risk_free_rate, market_return, smb, hml, rmw, cma):
    return (risk_free_rate + beta_m.mul(market_return - risk_free_rate, axis=0) +
            beta_smb.mul(smb, axis=0) + beta_hml.mul(hml, axis=0) +
            beta_rmw.mul(rmw, axis=0) + beta_cma.mul(cma, axis=0))

def pastor_stambaugh(beta_m, beta_smb, beta_hml, beta_liq, risk_free_rate, market_return, smb, hml, liq):
    return (risk_free_rate + beta_m.mul(market_return - risk_free_rate, axis=0) +
            beta_smb.mul(smb, axis=0) + beta_hml.mul(hml, axis=0) + beta_liq.mul(liq, axis=0))

def q_factor(beta_m, beta_me, beta_i, beta_roe, risk_free_rate, market_return, me, i, roe):
    return (risk_free_rate + beta_m.mul(market_return - risk_free_rate, axis=0) +
            beta_me.mul(me, axis=0) + beta_i.mul(i, axis=0) + beta_roe.mul(roe, axis=0))

def ccapm(beta_c, risk_free_rate, consumption_growth):
    return risk_free_rate + beta_c.mul(consumption_growth, axis=0)

def icapm(beta_m, beta_z, risk_free_rate, market_return, state_variables):
    return (risk_free_rate + beta_m.mul(market_return - risk_free_rate, axis=0) +
            beta_z.mul(state_variables, axis=0).sum(axis=1))

def sdf(expected_m, returns):
    return expected_m.mul(returns, axis=0)

def apt(beta_factors, risk_free_rate, factor_returns):
    return risk_free_rate + beta_factors.mul(factor_returns, axis=0).sum(axis=1)
