from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import PersistentStoreDatabaseSetting, PersistentStoreConnectionSetting


class GloEav(TethysAppBase):
    """
    Tethys app class for Environmental and Archeological Vulnerability.
    """

    name = 'Environmental and Archeological Vulnerability'
    index = 'glo_eav:home'
    icon = 'glo_eav/images/logo.jpg'
    package = 'glo_eav'
    root_url = 'glo-eav'
    color = '#16a085'
    description = 'Environmental and Archeological Vulnerability'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='glo-eav',
                controller='glo_eav.controllers.home'
            ),
            UrlMap(
                name='popup-info',
                url='glo-eav/popup-info',
                controller='glo_eav.controllers_ajax.get_popup_info'
            ),
            UrlMap(
                name='get-meta-file',
                url='glo-eav/get-meta-file',
                controller='glo_eav.controllers_ajax.get_meta_file'
            ),
            UrlMap(
                name='add-point',
                url='glo-eav/add-point',
                controller='glo_eav.controllers.add_point'
            ),
            UrlMap(
                name='delete-layer',
                url='glo-eav/delete-layer',
                controller='glo_eav.controllers.delete_layer'
            ),
            UrlMap(
                name='submit-delete-layer',
                url='glo-eav/delete-layer/submit',
                controller='glo_eav.controllers_ajax.layer_delete'
            ),
            UrlMap(
                name='add-point-ajax',
                url='glo-eav/add-point/submit',
                controller='glo_eav.controllers_ajax.point_add'
            ),
            UrlMap(
                name='approve-points',
                url='glo-eav/approve-points',
                controller='glo_eav.controllers.approve_points'
            ),
            UrlMap(
                name='approve-points_tabulator',
                url='glo-eav/approve-points/tabulator',
                controller='glo_eav.controllers_ajax.points_tabulator'
            ),
            UrlMap(
                name='update-points-ajax',
                url='glo-eav/approve-points/submit',
                controller='glo_eav.controllers_ajax.point_update'
            ),
            UrlMap(
                name='delete-points-ajax',
                url='glo-eav/approve-points/delete',
                controller='glo_eav.controllers_ajax.point_delete'
            ),
            UrlMap(
                name='add-polygon',
                url='glo-eav/add-polygon',
                controller='glo_eav.controllers.add_polygon'
            ),
            UrlMap(
                name='add-polygon-ajax',
                url='glo-eav/add-polygon/submit',
                controller='glo_eav.controllers_ajax.polygon_add'
            ),
            UrlMap(
                name='approve-polygons',
                url='glo-eav/approve-polygons',
                controller='glo_eav.controllers.approve_polygons'
            ),
            UrlMap(
                name='approve-polygons-tabulator',
                url='glo-eav/approve-polygons/tabulator',
                controller='glo_eav.controllers_ajax.polygons_tabulator'
            ),
            UrlMap(
                name='update-polygons-ajax',
                url='glo-eav/approve-polygons/submit',
                controller='glo_eav.controllers_ajax.polygon_update'
            ),
            UrlMap(
                name='delete-polygons-ajax',
                url='glo-eav/approve-polygons/delete',
                controller='glo_eav.controllers_ajax.polygon_delete'
            ),
            UrlMap(
                name='add-new-layer',
                url='glo-eav/add-new-layer',
                controller='glo_eav.controllers.add_new_layer'
            ),
            UrlMap(
                name='get-new-layer-attributes',
                url='glo-eav/add-new-layer/get-attributes',
                controller='glo_eav.controllers_ajax.get_shp_attributes'
            ),
            UrlMap(
                name='add-new-layer-ajax',
                url='glo-eav/add-new-layer/submit',
                controller='glo_eav.controllers_ajax.new_layer_add'
            ),
            UrlMap(
                name='set-layer-style',
                url='glo-eav/set-layer-style',
                controller='glo_eav.controllers.set_layer_style'
            ),
            UrlMap(
                name='set-layer-style-ajax',
                url='glo-eav/set-layer-style/submit',
                controller='glo_eav.controllers_ajax.layer_style_set'
            ),
            UrlMap(
                name='add-endpoint',
                url='glo-eav/add-endpoint',
                controller='glo_eav.controllers.add_endpoint'
            ),
            UrlMap(
                name='add-endpoint-submit',
                url='glo-eav/add-endpoint/submit',
                controller='glo_eav.controllers_ajax.endpoint_add'
            ),
            UrlMap(
                name='delete-endpoint',
                url='glo-eav/delete-endpoint',
                controller='glo_eav.controllers.delete_endpoint'
            ),
            UrlMap(
                name='delete-endpoint-submit',
                url='glo-eav/delete-endpoint/submit',
                controller='glo_eav.controllers_ajax.endpoint_delete'
            ),
            UrlMap(
                name='get-layers-info',
                url='glo-eav/api/get-layers-info',
                controller='glo_eav.api.get_layers_info'
            ),
            UrlMap(
                name='get-layers-by-county',
                url='glo-eav/api/get-layers-by-county',
                controller='glo_eav.api.get_layers_by_county'
            ),
            UrlMap(
                name='get-points-by-county',
                url='glo-eav/api/get-points-by-county',
                controller='glo_eav.api.get_points_by_county'
            ),
            UrlMap(
                name='get-polygons-by-county',
                url='glo-eav/api/get-polygons-by-county',
                controller='glo_eav.api.get_polygons_by_county'
            ),
            UrlMap(
                name='get-points-by-layer',
                url='glo-eav/api/get-points-by-layer',
                controller='glo_eav.api.get_points_by_layer'
            ),
            UrlMap(
                name='get-polygons-by-layer',
                url='glo-eav/api/get-polygons-by-layer',
                controller='glo_eav.api.get_polygons_by_layer'
            ),
            UrlMap(
                name='get-points-by-geometry',
                url='glo-eav/api/get-points-by-geometry',
                controller='glo_eav.api.get_points_by_geom'
            ),
            UrlMap(
                name='get-polygons-by-geometry',
                url='glo-eav/api/get-polygons-by-geometry',
                controller='glo_eav.api.get_polygons_by_geom'
            ),
            UrlMap(
                name='dowloand-layers',
                url='glo-eav/download-layers',
                controller='glo_eav.controllers_ajax.download_layers'
            ),
            UrlMap(
                name='download-interaction',
                url='glo-eav/download-interaction',
                controller='glo_eav.controllers_ajax.download_interaction'
            ),
            UrlMap(
                name='download-points-csv',
                url='glo-eav/api/download-points-csv',
                controller='glo_eav.api.download_points_csv'
            ),
            UrlMap(
                name='download-polygons-csv',
                url='glo-eav/api/download-polygons-csv',
                controller='glo_eav.api.download_polygons_csv'
            ),
            UrlMap(
                name='download-layer-csv',
                url='glo-eav/api/download-layer-csv',
                controller='glo_eav.api.download_layer_csv'
            ),
        )

        return url_maps

    def persistent_store_settings(self):
        """
        Define Persistent Store Settings.
        """
        ps_settings = (
            PersistentStoreDatabaseSetting(
                name='layers',
                description='layers database',
                initializer='glo_eav.model.init_layer_db',
                required=True,
                spatial=True
            ),
        )

        return ps_settings
