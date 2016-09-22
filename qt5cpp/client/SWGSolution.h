/**
 * Route Optimization API
 * Our Route Optimization API solves the so called vehicle routing problem fast. It calculates an optimal tour for a set of vehicles, services and constraints
 *
 * OpenAPI spec version: 1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

/*
 * SWGSolution.h
 * 
 * 
 */

#ifndef SWGSolution_H_
#define SWGSolution_H_

#include <QJsonObject>


#include "SWGRoute.h"
#include "SWGSolution_unassigned.h"
#include <QList>

#include "SWGObject.h"


namespace Swagger {

class SWGSolution: public SWGObject {
public:
    SWGSolution();
    SWGSolution(QString* json);
    virtual ~SWGSolution();
    void init();
    void cleanup();

    QString asJson ();
    QJsonObject* asJsonObject();
    void fromJsonObject(QJsonObject &json);
    SWGSolution* fromJson(QString &jsonString);

    qint32 getCosts();
    void setCosts(qint32 costs);
qint32 getDistance();
    void setDistance(qint32 distance);
qint64 getTime();
    void setTime(qint64 time);
qint64 getTransportTime();
    void setTransportTime(qint64 transport_time);
qint64 getMaxOperationTime();
    void setMaxOperationTime(qint64 max_operation_time);
qint64 getWaitingTime();
    void setWaitingTime(qint64 waiting_time);
qint32 getNoVehicles();
    void setNoVehicles(qint32 no_vehicles);
qint32 getNoUnassigned();
    void setNoUnassigned(qint32 no_unassigned);
QList<SWGRoute*>* getRoutes();
    void setRoutes(QList<SWGRoute*>* routes);
SWGSolution_unassigned* getUnassigned();
    void setUnassigned(SWGSolution_unassigned* unassigned);

private:
    qint32 costs;
qint32 distance;
qint64 time;
qint64 transport_time;
qint64 max_operation_time;
qint64 waiting_time;
qint32 no_vehicles;
qint32 no_unassigned;
QList<SWGRoute*>* routes;
SWGSolution_unassigned* unassigned;
};

} /* namespace Swagger */

#endif /* SWGSolution_H_ */
