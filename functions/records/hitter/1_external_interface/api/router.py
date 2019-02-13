from backup.controller.api import  ...and

class Router():

    @route(function_id='h01', path='/api/records/v1/hitter/{personal_id}', methon='get')
    def get_hitter_records(self, event, query, personal_id):
        """
        """
        name = query.get('name', None) if query is not None else None
        year = query.get('year', None) if query is not None else None

    @route(function_id='p01', path='/api/...', methon='get')
    def brabra(self, ):
        """
        """
        pass
