<template>
    <div :style="{backgroundImage:'url(https://www.designbolts.com/wp-content/uploads/2013/02/Textured-Stripes-Grey-Seamless-Patterns-For-Website-Background.jpg'}"
        class="d-flex flex-column align-items-center">

        <b-breadcrumb>
            <b-breadcrumb-item href="https://github.com/ssmith21">
                <b-icon icon="github" href="https://github.com/ssmith21" scale="1.25" shift-v="1.25" aria-hidden="true"></b-icon>
                My github
            </b-breadcrumb-item>
            <b-breadcrumb-item href="https://www.linkedin.com/in/seansmith514/">
                <b-icon icon="linkedin" href="https://www.linkedin.com/in/seansmith514/" scale="1.25" shift-v="1.25" aria-hidden="true"></b-icon>
                My Linkedin
            </b-breadcrumb-item>
        </b-breadcrumb>

        <div>
            <b-jumbotron 
            header="Stats and machine learning" 
            lead="Explore the process behind this webapp!"
            class="text-white jumbotron-image"
            style="background-image: url(https://images.unsplash.com/photo-1552152974-19b9caf99137?fit=crop&w=1350&q=80); max-width:80rem"
            > 
                <p>To go test out the calculator, click below</p>
                <b-button href="/" pill variant="light"><b>Calculator</b></b-button>
            </b-jumbotron>
        </div>

        <div>
            <b-card
                title="The data: Overview"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <img :src="images.xrotation">
                <b-card-text>
                The dataset used for training the machine learning model contains information from 30000 individuals.
                The goal is to determine the probability that in individual will default based on the following features:
                the balance limit on their credit card, gender, education, marital status, age, history of their past payments,
                amount of their bill statement and amount paid on their previous statement.
                There are 24 features in total, since some of the features are segmented into 6 different columns
                where each column represents their financial standing for a specific month.
                For more information on the dataset, visit the UCI Machine learning repository by clicking the button below:
                </b-card-text>
                <b-button href="https://archive.ics.uci.edu/ml/datasets/default+of+credit+card+clients" variant="primary">The dataset</b-button>
            </b-card>
        </div>

        <div style="max-width: 60rem;">
            <b-card
                title="The target"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <img class="smallimg" :src="images.img1">
                <b-card-text>
                Out of 30000 people, 6636 people defaulted on their credit card and 23364 did not. This means that 22.1% of credit card users become
                extremely delinquent with their payment. Predicting if an individual will default before they actually do is could be important
                information for the financial institutions who have credit card services.
                </b-card-text>
            </b-card>
        </div>

        <div style="max-width: 60rem;">
            <b-card
                title="First feature: Credit card balance limit"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <div 
                tag="article"
                class="mb-2"
                style="width: 57.5rem;">
                    <b-card no-body>
                        <b-tabs card>
                            <b-tab title="Description">
                                <b-card-title><code>Default=1</code> means credit card default next month.</b-card-title>
                                <b-card-text>
                                This feature is the amount of given credit for an individual and their families' credit if applicable.
                                We can see from the following 2 charts, that individuals with a lower amount of credit have a higher tendancy 
                                to default up until around 11000 credit, afterwhich those with a higher credit tend to dault more often.
                                There could be several explanations as to why this is. One of which could be that those with a lower credit limit
                                are able to reach their limit more easily, and may not be able to pay it off.
                                </b-card-text>
                            </b-tab>
                            <b-tab no-body title="Facetgrid of balance limit">
                                <img :src="images.img3">
                                <b-card-footer>Higher proportion of individuals default with a low balance limit</b-card-footer>
                            </b-tab>

                            <b-tab no-body title="Box plot of balance limit">
                                <img :src="images.img2">
                                <b-card-footer>Higher proportion of individuals default with a low balance limit</b-card-footer>
                            </b-tab>
                        </b-tabs>
                    </b-card>
                </div>
            </b-card>
        </div>

        <div style="max-width: 60rem;">
            <b-card
                title="Qualitative features of a cardholder"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <div>
                    <b-card no-body>
                        <b-tabs pills card vertical >             
                            
                            <b-tab title="Gender" style="max-width: 46.6rem;" active>
                                <b-card-text>
                                    <b>Who is more likely to default? Men or women?</b><br><br>
                                    According to this dataset, men are slightly more likely.
                                    Let A_i be a partition of the sample space of defaults in the study. 
                                    We partition the sample space as follows: A1=default, A2=no default. Let B be the set of all individuals of a certain gender. Then for i=1,2
                                </b-card-text>
                                <img :src="images.img5_1">
                                <b-card-text>
                                    However we only care about defaulting, so we get:
                                </b-card-text>
                                <img :src="images.img5_3">
                               <b-card-text>
                                    Probability of defaulting given the card owner is male : 24.17%<br>
                                    Probability of defaulting given the card owner is female :  20.78%                                
                                </b-card-text>
                                <img :src="images.img6">
                            </b-tab>

                            <b-tab title="Education" style="max-width: 46.6rem;" active>
                                <b-card-text>
                                    We can apply the same Bayesian logic to education as we did for gender.
                                </b-card-text>
                                <img :src="images.img5_2">
                                <b-card-text>
                                    where the prior is the empirical probability of a cardholder's education given a default.
                                    The results of this section shows that lower education level individuals have a higher chance of defaulting. 
                                    High school education individuals have a 25.16% of defaulting, 23.73% for university level education and 19.23% for grad school. 
                                    Due to limitted explanation of what the 'other' categories which have a 7.05% of defaulting, we omit an explanation.
                                </b-card-text>
                                <img :src="images.img7">

                            </b-tab>
                            <b-tab title="Marital status" style="max-width: 46.6rem;" active>
                                <b-card-text>
                                    Using the same method described in the other tabs, 
                                    we can observe that there is less discrepency between differing marital statuses on the effect of defaulting, 
                                    however it is worth noting that married individuals have a slightly higher chance of defaulting (23.47% versus 20.93%)
                                </b-card-text>
                                <img :src="images.img10">
                            </b-tab>
                            <b-tab title="Age" style="max-width: 46.6rem;" active>
                                <b-card-text>
                                    Individuals which are between the age of roughly 25-40 are less likely to default, 
                                    which is the age in which individuals most likely to be in the earlier stages of their careers. 
                                    Younger individuals are more likely to default, likely due to having lower income and/or less financial savy. 
                                    Older individuals have a higher chance of defaulting as well.
                                </b-card-text>
                                <img class="medimg" :src="images.img12">

                            </b-tab>
                            <b-tab title="Conclusion" style="max-width: 46.6rem;" active>
                                <b-card-text>
                                    It is difficult to say how much of an impact these qualitative features have on an individual defaulting.
                                    If a bank, or credit card company was manually calculating the chance that someone will default next month,
                                    this COULD be useful information, however it is unlikely that a model such as a neural network will
                                    assign much weight to these features as there simply isn't a clear and strong correlation between these
                                    features and an individual defaulting.
                                    
                                </b-card-text>
                            </b-tab>
                        </b-tabs>
                    </b-card>
                </div>

            </b-card>
        </div>


        <div style="max-width: 60rem;">
            <b-card
                title="Next 6 features: History of past payments by month"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <img class="medimg" :src="images.img13">
                <img class="medimg" :src="images.img23">
                <b-card-text>
                    These features represent the payment statuses of the individual holder for successive months. A value of -1 means they pay duly,
                    a value of 0 means they pay on the month their payment is due, a value of 1 means the payment of their bill was 1 month late,
                    2 means 2 months late etc... The data was presented in 6 columns, where each column represented a month, and the content of the column
                    was their payment status for that month. 
                    <br><br>An example of the distribution is shown in the picture directly above this text. The PAY_0 shows the facetgrid for
                    individuals and their repayment status in September, 2005. All the other columns follow a similar distribution.
                    <br><br><b>We can see that individuals that consistently pay on time have a less likely chance of defaulting
                    on their payment, either because they have some sort of automatic payment set up or they are have a routine habit of paying their bills.</b>
                    <br><br>We can also see from the sum payments that individuals who have a sum of payments equal to -1 or 0 over the course of all 6 months are 
                    much less likely to default.
                </b-card-text>
                <img class="smallimg" :src="images.img14">
            </b-card>
        </div>

        <div style="max-width: 60rem;">
            <b-card
                title="Next 6 features: Amount of bill statement"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <div 
                tag="article"
                class="mb-2"
                style="width: 57.5rem;">
                    <b-card no-body>
                        <b-tabs card>
                            <b-tab title="Description">
                                <b-card-text>
                                    The first column, BILL_AMT, is an individuals' bill statement amount on September 2005, the second column BILL_AMT2 is the 
                                    individual's bill statement on August 2005, etc... All the columns follow a very similar distribution.
                                    It is difficult to draw any immediate conclusions from just one of these columns, 
                                    or even the sum of all these columns. However if we look at the logsum, we get a more clear distribution.<br><br>
                                    By looking at all the columns, it appears the individuals with a high bill sum which increases over time, 
                                    or a bill sum of 0 are more prone to defaulting. This being said however, it's not a particularly
                                    strong indicator of whether or not an individual will default next month.<br><br>
                                    In the origional ipnyb notebook, I make the following observation however: 
                                    <b>For consecutive increasing time periods, if the bill sum remains high, the chance of defaulting next month.</b>
                                </b-card-text>
                            </b-tab>
                            <b-tab no-body title="Individual bill column = unclear">
                                <img class="medimg" :src="images.img25">
                                <b-card-footer>It's difficult draw any clear conclusions, let's look at the log-sum.</b-card-footer>
                            </b-tab>

                            <b-tab no-body title="Logsum of bills = more clarity!">
                                <img class="medimg" :src="images.img15">
                                <b-card-footer>This is more clear, but still not a strong indicator.</b-card-footer>
                            </b-tab>
                        </b-tabs>
                    </b-card>
                </div>
            </b-card>
        </div>

        <div style="max-width: 60rem;">
            <b-card
                title="Final 6 features: Payment amount"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <div 
                tag="article"
                class="mb-2"
                style="width: 57.5rem;">
                    <b-card no-body>
                        <b-tabs card>
                            <b-tab title="Description">
                                <b-card-text>
                                    This column consists of the amount the individual has paid on their previous payment. 
                                    PAY_AMT1 is the amount paid in September 2005, PAY_AMT2 is the amount paid in August 2005 etc...
                                    Looking at the facetgrids of the values makes it difficult to draw any conclusions due to the scaling 
                                    and variance of the values, so to visualise the data better, we take the log of each value and plot the facetgrids as such.
                                    <br><br>
                                    The log of the amount paid at each month is very indicative of whether an individual will default. 
                                    We see distinct spikes around the log(amount paid) of 0 and 7.5. for all the months.
                                    At these spike, there is a smaller chance of individuals defaulting.
                                    Looking at the log-sum, it is clear that individuals who pay a lower amount over the course of their history 
                                    have a higher chance of defaulting.
                                    This could potentially be because individuals who have the ability to pay more of their credit 
                                    card are less likely to default since they have the capital to do so.
                                </b-card-text>
                            </b-tab>
                            <b-tab no-body title="Individual pay amount = unclear">
                                <img class="medimg" :src="images.img26">
                                <b-card-footer>It's difficult draw any clear conclusions, let's look at the log-sum.</b-card-footer>
                            </b-tab>
                            <b-tab no-body title="Log of pay amount = more clarity!">
                                <img class="medimg" :src="images.img36">
                                <b-card-footer>This is more clear, but still not a strong indicator.</b-card-footer>
                            </b-tab>
                            <b-tab no-body title="Logsum of payments">
                                <img class="medimg" :src="images.img16">
                                <b-card-footer>This is more clear, but still not a strong indicator.</b-card-footer>
                            </b-tab>
                        </b-tabs>
                    </b-card>
                </div>
            </b-card>
        </div>


        <div style="max-width: 60rem;">
            <b-card
                title="Initial thoughts about the data"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <img class="medimg" :src="images.img17">
                <b-card-text>
                    We see that the PAY_i features have the highest correlation to whether or not the individual 
                    will default next month. 
                    Namely, PAY_0 has the highest correlation value, with 0.32 which the feature we added, 
                    PAY_LOGSUM has the second highest correlation value of 0.28. We can also see that another feature we added, 
                    BILL_LOGSUM has a relatively high correlation with the PAY_i columns. <br><br>
                    As seen in the correlation matrix below, unfortunately no major definitive conclusions can be drawn about 
                    predicting credit card defaults from the individual features
                    since there are no features which have a very high correlation with defaulting.
                </b-card-text>
            </b-card>
        </div>
        <br>

        <div>
            <b-jumbotron 
            header="Unsupervised learning" 
            lead="Now that we've explored the data, let's start looking at the machine learning concepts."
            class="text-white jumbotron-image"
            style="background-image: url(https://images.unsplash.com/photo-1552152974-19b9caf99137?fit=crop&w=1350&q=80); width:60rem"
            > 
            </b-jumbotron>
        </div>

        <div style="max-width: 60rem;">
            <b-card
                title="2 Component PCA reduction (standardized)"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <b-card-text>
                <b>How much information did we lose in PCA reduction?</b><br><br>
                As we reduce dimensionality, we lose information. Explained variance tells us how much information (variance) 
                can be attribute to each of the principal components. Using the attribute "explained_variance_ratio" 
                allows us to see the difference in variance. 30.12% of the information in (q1) 18.06% of the information in (q2) 
                Rest of the compoenents contain the rest of the information, so as we go down in dimension, we lose info. <br><br>
                So logically, we should include (q3) since it would increase how much information we have, but as we'll see, 
                not much variance is encapsulated in increase D' to 3 from 2.
                When we do this, we only gain 6% more information compared to the origional dataset. 
                In total, we can visualize 54% of the information in the data.
                </b-card-text>
                <img class="medimg" :src="images.img27">
                <img class="medimg" :src="images.img28">
            </b-card>
        </div>

        <div style="max-width: 60rem;">
            <b-card
                title="3 Component PCA reduction (standardized)"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <b-card-text>
                    In the 3D representation, it looks like there are 2 distinct clusters. 
                    The blue cluster is the cluster of defaulters, wheras the red dots are non-defaulters. 
                    The red dots 'surround' the cluster of blue dots, with a slight overlap between the two clusters. 
                    The blue dots also have lower values of PC2 and are close to the PC3 plane. 
                    They are also lower on the PC3 axis, wheras red dots are typically higher on the PC2 and PC3 axis. 
                    Along the PC1 axis, the two targets are jumbled up. We also see that, looking towards the PC3 axis, 
                    such that we see PC1 and PC2 as an X,Y plane, we can see distinct spikes formed by the two different targets.
                </b-card-text>
                <hr class="my-4">
                <img class="medimg" :src="images.xrotation">
                <hr class="my-4">
                <img class="medimg" :src="images.yrotation">
                <hr class="my-4">
                <img class="medimg" :src="images.zrotation">
            </b-card>
        </div>
        <br>

        <div>
            <b-jumbotron 
            header="Supervised Learning" 
            lead="How should we predict the chance of defaulting?"
            class="text-white jumbotron-image"
            style="background-image: url(https://images.unsplash.com/photo-1552152974-19b9caf99137?fit=crop&w=1350&q=80); width:60rem"
            > 
            </b-jumbotron>
        </div>

        <div style="max-width: 60rem;">
            <b-card
                title="Models"
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <div class="accordion" role="tablist">
                    <b-card no-body class="mb-1" style="width: 57.5rem;">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block v-b-toggle.accordion-1 variant="info">Logistic Regression</b-button>
                        </b-card-header>
                        <b-collapse id="accordion-1" visible accordion="my-accordion" role="tabpanel">
                            <b-card-body><b-card-text>
                                Logistic regression which uses l2 penalties, since we want to maximally penalize false binary predictions. <br>
                                We don't need to worry about outlier values since we have a binomial target.  <br>
                                Lbfgs solver gave the most consistent results during hyper-parameter tuning. <br> <br>
                                The model obtains a mean cross-validation accuracy of 79.9% with std=0.01729. 
                                According to the confusion matrix, we can see that it often predicts no-default when there is in-fact a default. 
                                This suggests that the model is biased towards predicting no-default given a datapoint. 
                                Since 22% of target values are 'default' and 78% are 'no-default', a validation accuracy of 79.9% 
                                is not much better than naively predicting 'default' 22% of the time. 
                                This could be due to the fact that it is difficult to obtain complex relationships using logistic regression and linear 
                                decision boundaries. <br><br>
                                Although we did not use the entire dataset for testing logistic regression, 
                                the evaluation on the partial dataset does not indicate that the model will perform particularly well on the dataset. <br>
                                <img :src="images.img29">
                            </b-card-text></b-card-body>
                        </b-collapse>
                    </b-card>

                    <b-card no-body class="mb-1" style="width: 57.5rem;">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block v-b-toggle.accordion-2 variant="info">K-Nearest Neighbours</b-button>
                        </b-card-header>
                        <b-collapse id="accordion-2" accordion="my-accordion" role="tabpanel">
                            <b-card-body><b-card-text>
                                We use k-nearest neighbours with k=30, as this returns the highest validation accuracy as shown in the figure below.<br>
                                <img :src="images.img30"><br>
                                Although KNN performs marginally better than logistic regression in this case (80.8% vs 79.9% mean cross validation accuracy), 
                                it suffers from a similar problem, as in it seems biased to predicting 'no-default'. 
                                It is also possible that the model performs better since it was trained on the entire dataset, 
                                rather than simply a sample, so a direct comparison may not be appropriate. <br>
                                <img :src="images.img31"><br>
                            </b-card-text></b-card-body>
                        </b-collapse>
                    </b-card>

                    <b-card no-body class="mb-1" style="width: 57.5rem;">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block v-b-toggle.accordion-3 variant="info">Kernel SVM</b-button>
                        </b-card-header>
                        <b-collapse id="accordion-3" accordion="my-accordion" role="tabpanel">
                            <b-card-body><b-card-text>
                                A support vector machine with an 'rbf' kernel was used in binary classification for predicting defaulters.
                                It is the best performing 'simple' model tested. 
                                It has the highest mean cross-validation accuracy of 81.7%, however it still has trouble predicting 
                                which individuals will default. Now we must try more powerful predictive models.
                                <img :src="images.img32"><br>
                            </b-card-text></b-card-body>
                        </b-collapse>
                    </b-card>

                    <b-card no-body class="mb-1" style="width: 57.5rem;">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block v-b-toggle.accordion-4 variant="info">Sparse Deep Neural Network</b-button>
                        </b-card-header>
                        <b-collapse id="accordion-4" accordion="my-accordion" role="tabpanel">
                            <b-card-body><b-card-text>
                                The default ADAM learning rate was found to be the best learning rate. 
                                Sigmoid activation function in the final layer was also tested against tanh and softmax, 
                                and sigmoid performed the best. As with the Dense neural network, swish gave higher validation accuracy than ReLu, 
                                and batch normalization and dropout was used to gain performance. It achieved a validation accuracy of 81.8%.
                                <img :src="images.img33"><br>
                                <img :src="images.img34"><br>
                            </b-card-text></b-card-body>
                        </b-collapse>
                    </b-card>

                    <b-card no-body class="mb-1" style="width: 57.5rem;">
                        <b-card-header header-tag="header" class="p-1" role="tab">
                            <b-button block v-b-toggle.accordion-5 variant="info">Dense Deep Neural Network</b-button>
                        </b-card-header>
                        <b-collapse id="accordion-5" accordion="my-accordion" role="tabpanel">
                            <b-card-body><b-card-text>
                                The default ADAM learning rate of 0.001 was found to be the best learning rate. 
                                Sigmoid activation function in the final layer was also tested against tanh and softmax, and sigmoid performed the best. 
                                The hidden layer activation functions are all swish, which performed better than ReLU by almost 1%. 
                                The same applies for the sparse neural network. Batch normalization and dropout was also tuned after many attempts. 
                                It achieved a validation accuracy of 82%.
                                <img :src="images.img35"><br>
                                <img :src="images.img37"><br>
                            </b-card-text></b-card-body>
                        </b-collapse>
                    </b-card>

                </div>

            </b-card>
        </div>

        <div style="max-width: 60rem;">
            <b-card
                tag="article"
                class="mb-2"
                style="max-width: 60rem;"
            >
                <b-card-text>
                    <h3><b>Models summary</b></h3>
                </b-card-text>
                <hr class="my-4">
                <b>Logistic regression</b><br>
                Baseline model: <code>79.9%</code> accuracy. Slow to train, underperforms.
                <hr class="my-4">
                <b>K-Nearest Neighbours</b><br>
                <code>80.8%</code> accuracy, fast to train, simple.
                <hr class="my-4">
                <b>SVM</b><br>
                Best performing 'simple' model, <code>81.7%</code> accuracy.
                <hr class="my-4">
                <b>Dense Neural Network</b><br>
                Best performing model overall, <code>82.1%</code> accuracy but slow to train.
                <hr class="my-4">
                <b>Sparse Neural Network</b><br>
                <code>81.8%</code> accuracy, but slowest to train.
                <hr class="my-4">
                <b>Unsupervised learning</b><br>
                2D PCA-Reduced Data is unable to classify between the two target values, 3D appeared to show clusters, but no clustering method gave definitive results.
                <hr class="my-4"><br>
                <b-card-text>
                    <h3><b>What we learned</b></h3>
                    <h5>Let's compare our pre-emptive data exploration with what our neural network has discovered.</h5>
                </b-card-text>
                <hr class="my-4">
                <h5>Quantitative data</h5>
                <hr class="my-4">
                <b>Paying and billing amounts</b><br>
                The individual who is least likely to default consistently has a high PAY_AMT, which suggests that the individual 
                always pays back their bills is least likely to default. 
                Furthermore, the payment amount AND billing amount is large, however when we look at the BILL_LOGSUM and PAY_LOGSUM, 
                we see that they are roughly equal (payment slightly higher than billed).
                The individual who is most likely to default has several months with no payment whatsoever, 
                with the exception of 1 small payment. Their sum of payments is much smaller than the sum of their billed amount. 
                Infact, this individual has a very similar billing sum to the individual who consistently pays it off, 
                however they do not pay their credit card bill.
                <hr class="my-4">
                <b>Payment timing</b><br>
                The individual who is least likely to default consistently pays duly. 
                In the pre-emptive data exploration, I stated my hypothesis for this reason: the individual who is 
                least likely to default has an automatic monthly payment system set-up, 
                or has a routine habit of paying off their bills on a certain day of the month.
                The individual who is most likely to default is consistently several months late with their payment. 
                At one point, the individual did not pay their credit card at all for 8 months.
                This confirms my findings in the pre-emptive data exploration, 
                which suggests that both the neural network model and I learned this feature correctly.
                <hr class="my-4">
                <b>Age</b><br>
                The individual who is least likely to default consistently has a high PAY_AMT, which suggests that the individual 
                always pays back their bills is least likely to default. 
                Furthermore, the payment amount AND billing amount is large, however when we look at the BILL_LOGSUM and PAY_LOGSUM, 
                we see that they are roughly equal (payment slightly higher than billed).
                The individual who is most likely to default has several months with no payment whatsoever, 
                with the exception of 1 small payment. Their sum of payments is much smaller than the sum of their billed amount. 
                Infact, this individual has a very similar billing sum to the individual who consistently pays it off, 
                however they do not pay their credit card bill.
                <hr class="my-4">
                <h5>Qualitative data</h5>
                <hr class="my-4">
                <b>Paying and billing amounts:</b><br>
                It is difficult to say if qualitative data is an indicator of whether or not an individual is likely to default or not. 
                Bayesian inference suggests that the probabilities of an individual defaulting changes with some of these qualities.
                In this case, the individual who is least likely to default matches the qualitative features found in the pre-emptive data exploration. 
                The same applies for the individual who is most likely to default, with the exception of education level, 
                however a higher ratio of university graduates defaulted compared to individuals with highschool-level education, 
                which I found to give the highest chance of defaulting.
            </b-card>
        </div>


    </div>
</template>


<script>
export default {
    data() {
        return {
            images: {
                img1: require('@/assets/img1.png'),
                img2: require('@/assets/img2.png'),
                img3: require('@/assets/img3.png'),
                img4: require('@/assets/img4.png'),
                img5_1: require('@/assets/img5_1.png'),
                img5_2: require('@/assets/img5_2.png'),
                img5_3: require('@/assets/img5_3.png'),
                img6: require('@/assets/img6.png'),
                img7: require('@/assets/img7.png'),
                img8: require('@/assets/img8.png'),
                img9: require('@/assets/img9.png'),
                img10: require('@/assets/img10.png'),
                img11: require('@/assets/img11.png'),
                img12: require('@/assets/img12.png'),
                img13: require('@/assets/img13.png'),
                img14: require('@/assets/img14.png'),
                img15: require('@/assets/img15.png'),
                img16: require('@/assets/img16.png'),
                img17: require('@/assets/img17.png'),
                img18: require('@/assets/img18.png'),
                img19: require('@/assets/img19.png'),
                img20: require('@/assets/img20.png'),
                img21: require('@/assets/img21.png'),
                img22: require('@/assets/img22.png'),
                img23: require('@/assets/img23.png'),
                img25: require('@/assets/img25.png'),
                img26: require('@/assets/img26.png'),
                img27: require('@/assets/img27.png'),
                img28: require('@/assets/img28.png'),
                img29: require('@/assets/img29.png'),
                img30: require('@/assets/img30.png'),
                img31: require('@/assets/img31.png'),
                img32: require('@/assets/img32.png'),
                img33: require('@/assets/img33.png'),
                img34: require('@/assets/img34.png'),
                img35: require('@/assets/img35.png'),
                img36: require('@/assets/img36.png'),                
                img37: require('@/assets/img37.png'),
                xrotation: require('@/assets/xrotation.gif'),
                yrotation: require('@/assets/yrotation.gif'),
                zrotation: require('@/assets/zrotation.gif'),
            }
        }
    },

}

</script>

<style>
.jumbotron-image { background-position: center center; background-repeat: no-repeat; background-size: cover }
.smallimg{height: 50%;width: 50%;}
.medimg{height: 95%;width: 95%;}
#img3{width:85%}
.pad { margin:5px; padding:5px; }
.pad2 { margin-bottom: 5px; margin-top: 5px; padding: 5px;}
.form-row{ justify-content: center ;}
#highrisk{color: rgb(126, 0, 0);}
#medrisk{color: rgb(0, 0, 214)}
#lowrisk{color: rgb(0, 92, 0)}
</style>