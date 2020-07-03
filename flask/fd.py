#!/usr/bin/env python
# coding: utf-8

# In[1]:


from flask import Flask, render_template, jsonify
app=Flask(__name__)


# In[3]:


@app.route("/")
@app.route("/home")
def home():
    return render_template('use.html')

@app.route('/background_process')
def background_process():
    return jsonify(result="working?")

if '__name__'=='__main__':
    app.run(debug=True)


# In[ ]:




