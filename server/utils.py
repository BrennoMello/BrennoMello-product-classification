def parse_request(data):
    """This function transforms the objet ProductRequest in a dictionary
        
        Parameters
        ----------
        data : ProductRequest
            The ProductRequest data
        
        Returns
        -------
        dict_pred :
            The dictionary in the format to model predict
            
    """

    dict_pred = {'title': []}
    for data in data.products:
        dict_pred['title'].append(data.title)
    
    return dict_pred