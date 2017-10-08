# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Neighborhood
                                 A QGIS plugin
 Seleccionar polígonos adyacentes
                             -------------------
        begin                : 2017-09-23
        copyright            : (C) 2017 by Juan Manuel Suarez Rodriguez / 20171094018
        email                : ingjuanmasuarez@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load Neighborhood class from file Neighborhood.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .neighbor import Neighborhood
    return Neighborhood(iface)
