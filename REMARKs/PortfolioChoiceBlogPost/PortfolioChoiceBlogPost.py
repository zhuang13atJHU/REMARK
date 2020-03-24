# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.6.9
#   latex_envs:
#     LaTeX_envs_menu_present: true
#     autoclose: false
#     autocomplete: false
#     bibliofile: biblio.bib
#     cite_by: apalike
#     current_citInitial: 1
#     eqLabelWithNumbers: true
#     eqNumInitial: 1
#     hotkeys:
#       equation: Ctrl-E
#       itemize: Ctrl-I
#     labels_anchors: false
#     latex_user_defs: false
#     report_style_numbering: false
#     user_envs_cfg: false
# ---

# %% [markdown]
# # Optimal Financial Investment over the Life Cycle
#
# <!-- [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/econ-ark/REMARK/master?filepath=REMARKs%2FPortfolioChoiceBlogPost%2FPortfolioChoiceBlogPost.ipynb) -->
#
# [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/econ-ark/REMARK/master?filepath=REMARKs%2FPortfolioChoiceBlogPost%2FPortfolioChoiceBlogPost.ipynb)
#
# Economists like to compare actual human behavior to the choices that would be made by a "rational" agent who optimally takes into account all the complexities of a decision.
#
# But for some problems, finding the optimal choice is remarkably difficult.  
#
# Financial decisions over a lifetime are such a problem.  Determining the optimal amount to save for retirement, and how much of your savings to invest in risky assets (like stocks) versus safe assets (like a bank account), turns out to be mathematically **much** harder than calculating how to land the Apollo spacecraft on the moon.  In fact, the computational tools that economists now use to solve such problems descend directly from those originally developed to optimize Apollo trajectories -- with 50 more years of development.
#
# By 2005, those tools were finally good enough to give financial advice that deserved to be taken seriously -- if by "taken seriously" we mean that economists's own personal decisions (and the advice they give to friends and family) were influenced by the results.  (A 2005 academic paper by [Cocco, Gomes, and Maenhout](https://doi.org/10.1093/rfs/hhi017) is now the standard reference.)
#
# But even today, these tools are so difficult that it can take years of study for a new researcher to master them; as a result, most economists studying consumer financial choices still do not use them.  
#
# In 2015, the U.S. [Consumer Financial Protection Bureau](https://www.consumerfinance.gov) funded the creation of the [Econ-ARK](https://econ-ark.org) open source software project, whose purpose is to make the mathematical tools for calculating optimal financial choices much more accessible, both to scholars and to the wider public.  Thanks to subsequent [funding by the Sloan Foundation](https://sloan.org) and the [Think Forward Institute](https://www.thinkforwardinitiative.com), the Econ-ARK team is proud to announce in this blog post the newest enhancement to our toolkit: It can now find the optimal solution to a lifetime optimal saving problem where the consumer can choose how much to invest in risky versus safe assets.
#
# Our hope is that transparent and publicly available tools like ours will eventually provide an alternative to the proprietary advice that has become widely available from "robo advisors" in the last few years (and has been available from human advisors much longer).

# %% [markdown]
# ## The Problem
#
# Nobody saving for retirement really knows what the future holds. They are likely to change jobs several times during their career, and each new job will have a different profile of income growth and risk; they might develop health problems that cut life short even before they reach retirement (in which case retirement savings would  be unnecessary), or they might turn out to be so healthy that they live to 100 (with a danger of outliving their savings).  
#
# Nor does anybody know what the payoffs will turn out to be for alternative investment choices.  "Risky" assets like stocks have historically earned higher returns than "safe" assets like government bonds -- but there is no guarantee that stocks will outperform bonds over any particular period (like, until you retire).
#
# Uncertainties like this are why the consumer's problem is so much harder than NASA's. The motion of a spacecraft is almost perfectly predictable:  If you point it in a certain direction with a certain velocity, Newton's equations can accurately predict where it will be far into the future.  In contrast, "optimal" behavior over a life that is subject to many risks must prudently take into account all of the possible outcomes.  
#
# "Big data" now allows us to quantify the risks associated with earnings from work: We can measure how often people change jobs at each age (taking into account differing personal characteristics like education, occupation and so on), and we can measure what happens to their income after job changes.  Job-related income uncertainty can therefore be represented mathematically as a statistical distribution over the many possible future outcomes, and similarly for other kinds of risk (like health risk). When all the biggest individual risks have been quantified, we can calculate the joint probabilities of every conceivable draw of the risks, and weight each possible outcome by its probability and its desirability.  Finally, we can calculate how the ultimate outcomes (like, retirement income) depend probabilisitcally on the current choice of saving and portfolio choice, and compute which choices would be "optimal" (in the sense of being the best available gamble) for consumers with different preferences (toward risk, for example).
#

# %% [markdown]
# ## The Solution
#
# ### Replicating the Standard Model
#
# The first use of our new `ConsPortfolioModel` has been to replicate the results of the above-mentioned 2005 paper (by Cocco, Gomes, and Maenhout - "CGM" for short).  For technical reasons our results are slightly different than theirs, but the "big-picture" findings are the same.
#
# A key input is a measure of the degree of consumers' ["risk aversion."](https://en.wikipedia.org/wiki/Risk_aversion)  Roughly speaking, risk aversion determines how much you are willing to pay to buy insurance against financial risks; or, if insurance is not available, how much you alter your behavior (for example, by saving more) as a precaution against the risk.  Researchers have found that many kinds of consumer behavior are consistent with values of "relative risk aversion" in the range from 2 to 4.  
#
# The most striking conclusion of the CGM paper is captured in the figure below.  We assume that consumers with typical risk aversion of 3 can choose between a "risky" asset with expected performance (for risk and return) like the stock market, versus a "safe" asset with lower expected returns historically typical of safe assets.  The figure shows, by age, the optimal risky share -- that is, the optimal proportion of savings that it would be optimal to invest in the "risky" asset.  The fact that the proportion is stuck at 1.0 at every age means that the computer says the optimal choice is always to invest 100 percent of your savings in stocks!
#
# <center><big>
#     Portfolio Choice for Moderately Risk Averse Consumer
#     </big>
# <center>
#     <img src='figures/figure_CRRA_3/RShare_Means.png'>
# </center>
#     
# <!-- ![RShare_CRRA_3](figures/figure_CRRA_3/RShare_Means.png) -->
#     

# %% [markdown]
# Of course, your optimal portfolio share in the risky asset depends on your _perception_ of the degree of riskiness and your _beliefs_ about the average extra return stocks will yield over the long run (the "equity premium").
#
# The model assumes that people expect an equity premium of 4 percent, which is a good estimate of what the average premium has been on stock market investments in the developed world over the past century.  (Risk is also assumed to match the historical average.)
#
# The model's conclusion is that for values of risk aversion that accurately capture people's risk-related choices in other contexts, an equity premium of 4 percent a year is more than enough to compensate almost any rational agent for bearing the risk that has typically been associated with that extra return.

# %% [markdown]
# ## Maybe Risk Aversion is Much Greater than 3?
#
# Parameters like "relative risk aversion" are slippery things to measure and calibrate.  Maybe the conventional choice of around 3, which works well to explain other choices, is inappropriate here -- maybe people just hate stock market risk much more than they hate other kinds of risk.
#
# The next figure shows the profile of the mean risky share for a consumer with risk aversion of 6, twice the conventional value.
#
# Even with such high risk aversion, the model says that until about age 35 it is still optimal to invest all of your savings in the stock market.  After that, the risky share declines gradually until it stabilizes at around 65 percent at age 65.  (The dashing lines show the choices made by people at the 5th and 95th percentiles of the distribution of the risky share).
#
# These results reflect two aspects of the model:
# 1. We assume that young people start with little or no assets
#    * Their income comes mostly from working in the labor market
#    * If you have only a small amount of wealth, the absolute dollar size of the risk you are taking by investing your (modest) retirement savings in the stock market is small, so the higher expected returns more than make up for the (small) risk
# 1. By the age of retirement, you plan to finance a lot of your spending from your savings
#    * Investing everything in the stock market would put a large proportion of your retirement spending at risk from market fluctuations
#    * The "equity premium" is nevertheless large enough to make it worthwhile for most people to keep half or more of their assets in stocks
#
# <!-- ![RShare_CRRA_3](figures/figure_CRRA_3/RShare_Means.png) -->
# <center><big>
#     Portfolio Choice for Highly Risk Averse Consumer
#     </big>
# <center>
#     <img src='figures/figure_Parameters_base/RShare_Means.png'>
# </center>
#     
# <!-- ![Parameters_base](figures/figure_Parameters_base/RShare_Means.png) -->

# %% [markdown]
# ## What Do People Actually Do?
#
# The pattern above is strikingly different from the actual choices that typical savers make.  
#
# The figure below shows data, from the Federal Reserve's triennial [_Survey of Consumer Finances_](https://en.wikipedia.org/wiki/Survey_of_Consumer_Finances), for the proportion of their assets that people at different ages actually have invested in stocks and other risky assets, taken from [this article](https://www.stlouisfed.org/publications/regional-economist/fourth-quarter-2018/role-age-investment-mix).
#
# The profile of the risky share in the data is much lower than the model says is optimal (even with extreme risk aversion of 6).
#
# Below we examine two possible interpretations:
# 1. The model is basically the right framework for thinking about these questions
#     * But some of its assumptions/calibrations are wrong
# 1. People _are_ behaving optimally, but the model is still missing some important features of reality
#
# <center>
#     <img src='figure_SCF-Risky-Share-By-Age/FedStLouis/vanderbroucke_fig1.jpg'>
# </center>
#
# <!-- ![SCF-Risky-Share-By-Age](figure_SCF-Risky-Share-By-Age/FedStLouis/vanderbroucke_fig1.jpg) -->
#

# %% [markdown]
# ### What Assumptions Might Be Wrong?
#
#

# %% [markdown]
# #### Maybe People Are Pessimistic About the Equity Premium
#
# While 4 percent is a good estimate of what the equity premium has been in the past, it is possible that most people do not _expect_ such a high equity premium (and never have expected it).
#
# The figure below shows the consequences if highly risk averse people believe the equity premium will be only two percent -- which is within the range of values that some respected economists believe might prevail in the future.
#
# The shape of the figure is much the same as before; in particular, the youngest people still hold 100 percent of their portfolios in risky assets.  But the proportion of their portfolios that middle-aged and older people hold in stocks falls from about 50 to about 20 percent.
#
# <center><big>
#     Pessimistic and Highly Risk Averse Consumer
#     </big>
# <center>
#     <img src='figures/figure_equity_0p02/RShare_Means.png'>
# </center>
#
#     
# <!-- ![RShare_Means](figures/figure_equity_0p02/RShare_Means.png) -->
#

# %% [markdown]
# #### Is Pessimism Enough?
#
# The preceding figure assumes that relative risk aversion is very high (6).  A natural question is whether, when people are pessimistic about the equity premium, their optimal portfolio shares might be low even at a less extreme degree of risk aversion.  
#
# Nope.  The figure below shows that, even with pessimistic beliefs about the equity premium, if relative risk aversion has a conventional value of 3 then the optimal risky share is still 100 percent for both young and old people, and on average reaches a low point of about 90 percent for people nearing retirement.
#
# <center><big>
#     Pessimistic and Moderately Risk Averse Consumer
#     </big>
# <center>
#     <img src='figures/figure_CRRA_3_Equity_Premium_2/RShare_Means.png'>
# </center>
#
#
# <!-- ![CRRA_3_Equity_Premium_2](figures/figure_CRRA_3_Equity_Premium_2/RShare_Means.png) -->

# %% [markdown]
# ### Comparison to Professional Advice

# %% [markdown]
# Another interesting comparison is to the advice of professional investment advisors.  Though that advice can be quite sophistcated and nuanced, it is also sometimes codified in simple rules of thumb.  One of the most common of these is the "100 minus age" rule, which says that the percentage of your portfolio in risky assets should be equal to 100 minus your age; a 25 year old would have 75 percent in stocks while a 60 year old would have 40 percent in stocks.
#
# For people before retirement, the shape of the profile that advisors recommend is somewhat like the shape that comes out of the model (assuming high risk aversion).  While the advisors' rule would say that the 25 year old should put 75 percent of their savings in the stock market and the model says 100 percent, they agree that the young person's proportion should be high, and also agree that the proportion should decline during working life.
#
# However, the rule and the model disagree about what should happen after retirement.  The rule recommends steadily reducing your exposure to risky assets as you get older, while the model says that after retirement your exposure should remain at about the same level it was late in your working life.
#
# Financial advisors, who have daily contact with real human beings, may have an insight that the model does not incorporate:  Perhaps risk aversion increases as you get older.  
#
# Risk aversion is remarkably difficult to measure, and economists' efforts to determine whether it increases with age have been inconclusive, with some studies finding [evidence for an increase](https://voxeu.org/article/effect-age-willingness-take-risks) (at least during working life) and others finding [little increase](https://onlinelibrary.wiley.com/doi/abs/10.1016/j.rfe.2003.09.010).  (New research suggests that any increases in risk aversion among older people reflect [cognitive decline](https://www.nature.com/articles/ncomms13822) associated with reduced ability to process information.) 
#
# For technical reasons, it is somewhat difficult to incorporate values of risk aversion that vary directly with age.  But your willingness to invest in risky assets depends on both your degree of aversion to risk and your perception of the size of the risk.  So a backdoor way to examine the consequences of rising risk aversion with age is to assume that the perceived riskiness of stock investments goes up with age.  
#
# That is what is done in the figure below: We assume that the perceived riskiness of stock market investment doubles between age 65 and age 100.  The result now looks more like the advice of financial advisors:  Increasing _perceived_ risk as you get older persuades you to invest less in risky assets.
#
# This figure suggests that the "100 minus age" rule is not too bad as an approximation of what an extremely risk averse person might want to do -- if they become more and more fearful as they age after retirement.  
#
# <center><big>
#     100 Minus Age Rule vs Optimizing Highly Risk Averse Consumer
#     </big>
# <center>
#     <img src='figures/figure_risky_age/RShare_Means_100_age.png'>
# </center>
#
# <!-- ![risky_age](figures/figure_risky_age/RShare_Means_100_age.png) -->

# %% [markdown]
# ### Other Experiments
#
# The `ConsPortfolioModel` tool makes it easy to explore other alternatives.  For example, after the CGM paper was published, better estimates [became available](https://doi.org/10.1016/j.jmoneco.2010.04.003) about the degree and types of income uncertainty that consumers face at different ages.  The most important finding was that the degree of uncertainty in earnings is quite large for people in their 20s but falls sharply then flattens out at older ages.  
#
# It seems plausible that this greater uncertainty in labor earnings could account for the fact that in empirical data young people have a low share of their portfolio invested in risky assets; economic theory says that an increase in labor income risk should [reduce your willingness to expose yourself to financial risk](https://www.jstor.org/stable/2951719).
#
# But the figure below shows that even when we update the model to incorporate the improved estimates of labor income uncertainty, the model still says that young people should have 100 percent of their savings in the risky asset.
#
#
# <center><big>
#     Using Better Data on Income Risk By Age
#     </big>
# <center>
#     <img src='figures/figure_Parameters_1940s_shocks/RShare_Means.png'>
# </center>
#
# <!-- ![Parameters_1940s_shocks](figures/figure_Parameters_1940s_shocks/RShare_Means.png) --> 
#
# Many other experiments are possible in the framework, but the conclusion is always the same: Even if people expect that stock returns in the future will be substantially lower than they have been in the past, for most people most of the time, the return on stock market investments more than compensates for any reasonable degree of risk aversion.

# %% [markdown]
# #### What Might Still Be Missing
#
# Some experiments are NOT yet possible with our toolkit.  Perhaps the most important is that we have no way to take into account the risks entailed in homeownership.  Houses, like stocks, are assets whose price can go up or down.  Since housing wealth constitutes the majority of the wealth of most consumers, the model's failure to take into account the effects that homeownership should have on the optimal choice of risky investment in other (non-housing) forms is a serious enough failing to call into question the soundness of its conclusions.  
#
# The Think Forward Institute grant that funded this work has a second component:  The addition of a realistic treatment of the effects of home ownership on the optimal share of financial investment in risky assets.  This is a question that is at the frontier of what is possible using the kinds of tools we are developing.  We are interested to see whether a proper treatment of homeownership will be enough to temper the recommendations of the model to invest heavily in other risky assets.  The answer is not clear -- which is why we need a model!

# %% [markdown]
# #### Code
#
# The computer code to reproduce all of the figures in this notebook, and a great many others, can be executed by [installing](https://github.com/econ-ark/HARK/#install) the [Econ-ARK toolkit](https://github.com/econ-ark/HARK/#readme) and cloning the [REMARK](https://github.com/econ-ark/REMARK) repository.  The small unix program `do_all_code.sh` at the root level of the [REMARKs/PortfolioChoiceBlogPost](https://github.com/econ-ark/REMARK/blob/master/REMARKs/PortfolioChoiceBlogPost/do_all_code.sh) directory produces everything.
#
# A replication of main results of the CGM paper is referenced in a link below.
#
# The [Econ-ARK](https://github.com/econ-ark) toolkit is available at GitHub, and [the `ConsPortfolioModel`](https://github.com/econ-ark/HARK/blob/master/HARK/ConsumptionSaving/ConsPortfolioModel.py) is [documented here](https://hark.readthedocs.io/en/latest/example_notebooks/ConsPortfolioModel.html).

# %% [markdown]
# #### References
#
# Cocco, J. F., Gomes, F. J., & Maenhout, P. J. (2005). Consumption and portfolio choice over the life cycle. The Review of Financial Studies, 18(2), 491-533.  [doi.org/10.1093/rfs/hhi017](https://doi.org/10.1093/rfs/hhi017)
#
# Velásquez-Giraldo, Mateo and Matthew Zahn.  Replication of Cocco, Gomes, and Maenhout (2005).  [REMARK](https://github.com/econ-ark/REMARK/blob/master/REMARKs/CGMPortfolio/Code/Python/CGMPortfolio.ipynb)
