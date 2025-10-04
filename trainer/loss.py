import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models

def custom_loss(y_true, y_pred, specs):
    """
    y_true: [indice_total_real, num_modulos_real]
    y_pred: [indice_total_pred, num_modulos_pred]
    specs: dicionário com dados do módulo e inversor para checagens
    """
    
    index_pred = y_pred[:, 0]
    nmod_pred = tf.round(y_pred[:, 1])  
    
    index_true = y_true[:, 0]
    nmod_true = y_true[:, 1]
    
    loss_indice = tf.reduce_mean(tf.square(indice_true - indice_pred))
    loss_mod = tf.reduce_mean(tf.square(num_mod_true - num_mod_pred))
    
    Voc_total = specs["Voc_mod"] * num_mod_pred
    Vmp_total = specs["Vmp_mod"] * num_mod_pred
    
    penalty_voltage = tf.reduce_mean(
        tf.cast(tf.logical_or(
            Voc_total > specs["Vmax_inv"],
            Vmp_total < specs["Vmin_inv"]
        ), tf.float32) * 10.0  # weight
    )
    
    total_loss = loss_indice + loss_mod + penalty_voltage
    
    return total_loss