/* 
 * Route Optimization API
 *
 * Our Route Optimization API solves the so called vehicle routing problem fast. It calculates an optimal tour for a set of vehicles, services and constraints
 *
 * OpenAPI spec version: 1.0
 * 
 * Generated by: https://github.com/swagger-api/swagger-codegen.git
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

using System;
using System.Linq;
using System.IO;
using System.Text;
using System.Collections;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using System.Runtime.Serialization;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace IO.Swagger.Model
{
    /// <summary>
    /// Route
    /// </summary>
    [DataContract]
    public partial class Route :  IEquatable<Route>
    {
        /// <summary>
        /// Initializes a new instance of the <see cref="Route" /> class.
        /// </summary>
        /// <param name="VehicleId">id of vehicle that operates route.</param>
        /// <param name="Distance">distance of route in meter.</param>
        /// <param name="TransportTime">transport time of route in ms.</param>
        /// <param name="CompletionTime">completion time of route in ms.</param>
        /// <param name="WaitingTime">waiting time of route in ms.</param>
        /// <param name="Activities">array of activities.</param>
        public Route(string VehicleId = null, long? Distance = null, long? TransportTime = null, long? CompletionTime = null, long? WaitingTime = null, List<Activity> Activities = null)
        {
            this.VehicleId = VehicleId;
            this.Distance = Distance;
            this.TransportTime = TransportTime;
            this.CompletionTime = CompletionTime;
            this.WaitingTime = WaitingTime;
            this.Activities = Activities;
        }
        
        /// <summary>
        /// id of vehicle that operates route
        /// </summary>
        /// <value>id of vehicle that operates route</value>
        [DataMember(Name="vehicle_id", EmitDefaultValue=false)]
        public string VehicleId { get; set; }
        /// <summary>
        /// distance of route in meter
        /// </summary>
        /// <value>distance of route in meter</value>
        [DataMember(Name="distance", EmitDefaultValue=false)]
        public long? Distance { get; set; }
        /// <summary>
        /// transport time of route in ms
        /// </summary>
        /// <value>transport time of route in ms</value>
        [DataMember(Name="transport_time", EmitDefaultValue=false)]
        public long? TransportTime { get; set; }
        /// <summary>
        /// completion time of route in ms
        /// </summary>
        /// <value>completion time of route in ms</value>
        [DataMember(Name="completion_time", EmitDefaultValue=false)]
        public long? CompletionTime { get; set; }
        /// <summary>
        /// waiting time of route in ms
        /// </summary>
        /// <value>waiting time of route in ms</value>
        [DataMember(Name="waiting_time", EmitDefaultValue=false)]
        public long? WaitingTime { get; set; }
        /// <summary>
        /// array of activities
        /// </summary>
        /// <value>array of activities</value>
        [DataMember(Name="activities", EmitDefaultValue=false)]
        public List<Activity> Activities { get; set; }
        /// <summary>
        /// Returns the string presentation of the object
        /// </summary>
        /// <returns>String presentation of the object</returns>
        public override string ToString()
        {
            var sb = new StringBuilder();
            sb.Append("class Route {\n");
            sb.Append("  VehicleId: ").Append(VehicleId).Append("\n");
            sb.Append("  Distance: ").Append(Distance).Append("\n");
            sb.Append("  TransportTime: ").Append(TransportTime).Append("\n");
            sb.Append("  CompletionTime: ").Append(CompletionTime).Append("\n");
            sb.Append("  WaitingTime: ").Append(WaitingTime).Append("\n");
            sb.Append("  Activities: ").Append(Activities).Append("\n");
            sb.Append("}\n");
            return sb.ToString();
        }
  
        /// <summary>
        /// Returns the JSON string presentation of the object
        /// </summary>
        /// <returns>JSON string presentation of the object</returns>
        public string ToJson()
        {
            return JsonConvert.SerializeObject(this, Formatting.Indented);
        }

        /// <summary>
        /// Returns true if objects are equal
        /// </summary>
        /// <param name="obj">Object to be compared</param>
        /// <returns>Boolean</returns>
        public override bool Equals(object obj)
        {
            // credit: http://stackoverflow.com/a/10454552/677735
            return this.Equals(obj as Route);
        }

        /// <summary>
        /// Returns true if Route instances are equal
        /// </summary>
        /// <param name="other">Instance of Route to be compared</param>
        /// <returns>Boolean</returns>
        public bool Equals(Route other)
        {
            // credit: http://stackoverflow.com/a/10454552/677735
            if (other == null)
                return false;

            return 
                (
                    this.VehicleId == other.VehicleId ||
                    this.VehicleId != null &&
                    this.VehicleId.Equals(other.VehicleId)
                ) && 
                (
                    this.Distance == other.Distance ||
                    this.Distance != null &&
                    this.Distance.Equals(other.Distance)
                ) && 
                (
                    this.TransportTime == other.TransportTime ||
                    this.TransportTime != null &&
                    this.TransportTime.Equals(other.TransportTime)
                ) && 
                (
                    this.CompletionTime == other.CompletionTime ||
                    this.CompletionTime != null &&
                    this.CompletionTime.Equals(other.CompletionTime)
                ) && 
                (
                    this.WaitingTime == other.WaitingTime ||
                    this.WaitingTime != null &&
                    this.WaitingTime.Equals(other.WaitingTime)
                ) && 
                (
                    this.Activities == other.Activities ||
                    this.Activities != null &&
                    this.Activities.SequenceEqual(other.Activities)
                );
        }

        /// <summary>
        /// Gets the hash code
        /// </summary>
        /// <returns>Hash code</returns>
        public override int GetHashCode()
        {
            // credit: http://stackoverflow.com/a/263416/677735
            unchecked // Overflow is fine, just wrap
            {
                int hash = 41;
                // Suitable nullity checks etc, of course :)
                if (this.VehicleId != null)
                    hash = hash * 59 + this.VehicleId.GetHashCode();
                if (this.Distance != null)
                    hash = hash * 59 + this.Distance.GetHashCode();
                if (this.TransportTime != null)
                    hash = hash * 59 + this.TransportTime.GetHashCode();
                if (this.CompletionTime != null)
                    hash = hash * 59 + this.CompletionTime.GetHashCode();
                if (this.WaitingTime != null)
                    hash = hash * 59 + this.WaitingTime.GetHashCode();
                if (this.Activities != null)
                    hash = hash * 59 + this.Activities.GetHashCode();
                return hash;
            }
        }
    }

}
