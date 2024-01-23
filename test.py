import joblib
import sys
import pickle


# from features_extraction import LOCALHOST_PATH, DIRECTORY_NAME


def get_prediction_from_url(test_url):

    # obj = FeatureExtraction(test_url)
    # res = {}
    # res = obj.getFeaturesDict()
    vectorizer = pickle.load(open('vector1.pickle','rb'))
    features_test = vectorizer.transform([test_url])
    # # Due to updates to scikit-learn, we now need a 2D array as a parameter to the predict function.
    # features_test = np.array(features_test).reshape((1, -1))

    clf = joblib.load('classifier/random_forest_urls_finaltry1.pkl')
    
    pred = clf.predict(features_test)
    return int(pred[0])


def main(arg):
    
    # url = sys.argv[1]
    url = arg
    prediction = get_prediction_from_url(url)

    # Print the probability of prediction (if needed)
    # prob = clf.predict_proba(features_test)
    # print 'Features=', features_test, 'The predicted probability is - ', prob, 'The predicted label is - ', pred
    #    print "The probability of this site being a phishing website is ", features_test[0]*100, "%"

    if prediction == 0:
        # print "The website is safe to browse"
        print("SAFE")
    elif prediction ==1:
        # print "The website has phishing features. DO NOT VISIT!"
        print("PHISHING")

        # print 'Error -', features_test


if __name__ == "__main__":
    main(sys.argv[1])