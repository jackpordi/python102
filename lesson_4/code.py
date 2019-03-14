from sklearn.ensemble import RandomForestRegressor

rf = RandomForestRegressor()
rf.fit(train_x, train_y)

pred_y = rf.predict(test_y)

# Now compare pred_y and actual test_y
